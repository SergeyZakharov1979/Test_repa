def is_valid_triangle(s1, s2, s3):
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        return True
    else:
        return False
    

print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
