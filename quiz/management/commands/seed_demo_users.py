from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from teacher.models import Teacher
from student.models import Student


class Command(BaseCommand):
    help = "Creates demo Admin (Sawera), Teacher (Rehan), and Student (Ali) accounts for the Online Quiz Management System."

    def handle(self, *args, **options):
        # Make sure the groups used by the app exist
        teacher_group, _ = Group.objects.get_or_create(name='TEACHER')
        student_group, _ = Group.objects.get_or_create(name='STUDENT')

        # ---------- Admin: Sawera ----------
        if not User.objects.filter(username='sawera').exists():
            admin_user = User.objects.create_superuser(
                username='sawera',
                email='sawera@example.com',
                password='Sawera@123',
                first_name='Sawera',
                last_name='Admin'
            )
            self.stdout.write(self.style.SUCCESS('Admin "Sawera" created (username: sawera / password: Sawera@123)'))
        else:
            self.stdout.write('Admin "Sawera" already exists, skipping.')

        # ---------- Teacher: Rehan ----------
        if not User.objects.filter(username='rehan').exists():
            teacher_user = User.objects.create_user(
                username='rehan',
                email='rehan@example.com',
                password='Rehan@123',
                first_name='Rehan',
                last_name='Teacher'
            )
            teacher_user.groups.add(teacher_group)
            Teacher.objects.create(
                user=teacher_user,
                address='Lahore, Pakistan',
                mobile='03001234567',
                status=True,     # pre-approved so login works immediately
                salary=50000
            )
            self.stdout.write(self.style.SUCCESS('Teacher "Rehan" created (username: rehan / password: Rehan@123)'))
        else:
            self.stdout.write('Teacher "Rehan" already exists, skipping.')

        # ---------- Student: Ali ----------
        if not User.objects.filter(username='ali').exists():
            student_user = User.objects.create_user(
                username='ali',
                email='ali@example.com',
                password='Ali@123',
                first_name='Ali',
                last_name='Student'
            )
            student_user.groups.add(student_group)
            Student.objects.create(
                user=student_user,
                address='Karachi, Pakistan',
                mobile='03007654321'
            )
            self.stdout.write(self.style.SUCCESS('Student "Ali" created (username: ali / password: Ali@123)'))
        else:
            self.stdout.write('Student "Ali" already exists, skipping.')

        self.stdout.write(self.style.SUCCESS('Demo users are ready.'))
