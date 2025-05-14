
def turing_machine(input_tape):
    # تحويل النص إلى قائمة لتمثيل شريط آلة تورنغ
    tape = list(input_tape)
    
    head = 0
    
    while head < len(tape):
        # إذا وصلنا إلى علامة +
        if tape[head] == '+':
            # نحذف علامة +
            tape.pop(head)
            # الآن الرأس يشير إلى الرقم الثاني مباشرة بعد حذف +
            # نكمل من نفس الموضع لأن باقي العناصر انزاحت لليسار
            break
        else:
            # الانتقال إلى الخلية التالية
            head += 1
    
    # بعد إزالة علامة +، يكون لدينا كل الرموز في تسلسل واحد، لكن الحجم الأصلي قل بواحد
    # النتيجة هي الشريط بعد الدمج (كل 1s بدون +)
    result = ''.join(tape)
    return result

# اختبار الدالة
input_str = "111+11"
output = turing_machine(input_str)
print("Output:",output)