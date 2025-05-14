grammar = {
    'S': [['A', 'B']],        # القاعدة: S → A B
    'A': [['a'], ['a', 'A']], # القاعدة: A → a | a A
    'B': [['b']]              # القاعدة: B → b
}

# الجملة التي نريد تحليلها
sentence = ['a', 'a', 'b']  

#  دالة للتحقق إذا كان الرمز Non-terminal
def is_non_terminal(sym):
    return sym in grammar  # إذا كان الرمز موجود في القواعد، يعني هو non-terminal.

# دالة parse تحاول توليد جميع أشجار التحليل الممكنة
# هذه الدالة تقوم بتحليل الجملة ابتداءً من الرمز غير الطرفي (sym) في الموضع i.
def parse(sym, i):
    if i > len(sentence):  # إذا تجاوزنا نهاية الجملة، نرجع قائمة فارغة.
        return []

    if not is_non_terminal(sym):  # إذا كان الرمز طرفيًا (مثل 'a' أو 'b')
        if i < len(sentence) and sentence[i] == sym:  # إذا تطابق الرمز مع الكلمة الحالية في الجملة
            return [([sym], i + 1)]  # نرجع شجرة تحتوي على هذا الرمز وننتقل للموقع التالي في الجملة.
        else:
            return []  # إذا لم يكن هناك تطابق، نرجع قائمة فارغة.

    results = []  # لتخزين جميع الأشجار الممكنة
    for rule in grammar[sym]:  # لكل إنتاج للرمز الحالي
        trees = [([], i)]  # نبدأ من موضع i ونحلل بشكل فارغ في البداية
        for part in rule:  # نحلل كل جزء في الإنتاج (مثل 'a' أو 'A')
            new_trees = []  # قائمة لتخزين الأشجار الجديدة الناتجة من التحليل
            for t, j in trees:  # t: شجرة مؤقتة، j: الموضع الحالي في الجملة
                for sub_tree, k in parse(part, j):  # نحاول تحليل الجزء الحالي
                    new_trees.append((t + [sub_tree], k))  # نضيف النتيجة الجديدة
            trees = new_trees  # نحدث الأشجار المؤقتة
        results += [([sym] + t, j) for t, j in trees]  # نضيف الأشجار الناتجة من التحليل في هذا الإنتاج

    return results  # نرجع جميع الأشجار الممكنة

# 5. محاولة تحليل الجملة ابتداء من الرمز غير الطرفي 'S' ومن أول كلمة في الجملة
all_trees = [t for t, j in parse('S', 0) if j == len(sentence)]  # نحتفظ بالأشجار التي تصل لنهاية الجملة

# 6. طباعة عدد الأشجار الناتجة
print("Number of analysis tree :", len(all_trees))

# 7. التحقق إذا كانت القواعد غامضة
if len(all_trees) > 1:
    print("The grammar is ambiguous for this sentence")  # إذا كانت هناك أكثر من شجرة تحليل، القواعد غامضة.
elif len(all_trees) == 1:
    print("The grammar is not ambiguous for this sentence")  # إذا كانت هناك شجرة تحليل واحدة، القواعد غير غامضة.
else:
    print("The sentence does not belong to these rules")  # إذا لم نتمكن من تحليل الجملة.

# 8. طباعة الأشجار الناتجة
for i, tree in enumerate(all_trees):
    print(f"\n  tree number = {i+1} and she is : {tree}")
    