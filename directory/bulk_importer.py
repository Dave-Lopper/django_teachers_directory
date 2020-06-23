from django.core.files import File
from zipfile import ZipFile

from .models import Subject, Teacher
from teachers_directory.settings import AVATAR_UPLOAD_FOLDER


def bulk_insert(csv_file, zip_file):
    """Inserts many teachers from CSV

    Args:
        csv_file [_csv.reader]: The CSV file received from form, read
        zip_file [django.core.files.uploadedfile.InMemoryUploadedFile]:
            The ZIP file received from form

    Returns:
        [int]: command like return code depending on the CSV's content
    """
    teachers = []
    filtered_data = list(
        filter(
            lambda x: x[0] != '' and x[1] != '' and x[3] != '' and x[4] != '',
            list(csv_file)
        )
    )
    if len(filtered_data) < 1:
        return 1

    line_count = 0
    for row in filtered_data:
        if line_count == 0:
            columns = row
        else:
            for index in range(len(row)):
                if index == 0:
                    teachers.append({
                        columns[index]: row[index]
                    })
                else:
                    if columns[index] == "Subjects taught":
                        teachers[line_count - 1][columns[index]] = \
                            row[index].split(',')[0:5]
                    else:
                        teachers[line_count - 1][columns[index]] = row[index]
        line_count += 1

    with ZipFile(zip_file, 'r') as zip:
        for teacher in teachers:
            subjects = []
            for subject in teacher['Subjects taught']:
                fetched_subject = Subject.objects.filter(
                    name=subject.strip().capitalize()
                ).first()
                if fetched_subject is not None:
                    subjects.append(fetched_subject)
                else:
                    new_subject = Subject.objects.create(
                        name=subject.strip().capitalize()
                    )
                    subjects.append(new_subject)
            if len(subjects) > 0 and Teacher.objects.filter(
                    email=teacher["Email Address"]
            ).count() == 0:
                new_teacher = Teacher.objects.create(
                    first_name=teacher["First Name"],
                    last_name=teacher["Last Name"],
                    email=teacher["Email Address"],
                    phone=teacher["Phone Number"],
                    room=teacher["Room Number"]
                )
                new_teacher.subjects.set(subjects)
                if teacher["Profile picture"] in zip.namelist():
                    location = AVATAR_UPLOAD_FOLDER + teacher["Profile picture"]  # noqa:E501

                    zip.extract(
                        teacher["Profile picture"],
                        AVATAR_UPLOAD_FOLDER
                    )
                    new_teacher.profile_picture.save(
                        location,
                        File(open(location, 'rb'))
                    )
                new_teacher.save()
        return 0
