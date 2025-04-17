def generateParenthesis(n):

    root = '()'
    for _ in range(n - 1):
        root = f'({root})'

    result_set = set()
    staged = []
        
    staged.append(root)
    result_set.add(root[:])
    
    while len(staged) > 0:

        substitution_possible = False

        # Find 1st substring
        parent = staged[0]
        new = parent.replace('(())', '()()')
        print(new)
        if new != parent and new not in result_set:
            # Sub ... new string created
            staged.append(new)
            result_set.add(new[:])
        else:
            # Check for second sub
            new1 = parent.replace('((()))', '()(())')
            new2 = parent.replace('((()))', '(())()')
            if new1 != parent and new1 not in result_set:
                staged.append(new1)
                result_set.add(new1[:])
                substitution_possible = True
            if new2 != parent and new2 not in result_set:
                staged.append(new2)
                result_set.add(new2[:])
                substitution_possible = True
            if not substitution_possible:
                staged.pop(0)

        print(result_set)
        
    return list(result_set)
        
        
generateParenthesis(3)