from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_app.models import Student
from library_app.models import LibraryRecord
from payment_app.models import Payment

@api_view(['GET'])
def student_summary(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})

    library = LibraryRecord.objects.filter(student_id=student_id).first()
    payments = Payment.objects.filter(student_id=student_id)

    total_paid = sum([p.amount_paid for p in payments])

    data = {
        "student": {
            "id": student.student_id,
            "name": student.name,
            "course": student.course
        },
        "library": {
            "has_fines": library.has_fines if library else False,
            "amount_due": float(library.amount_due) if library else 0
        },
        "payments": {
            "total_paid": float(total_paid)
        }
    }

    return Response(data)
