# 6) Convert Pascal Case string into snake_case (4 ქულა)

# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

def pascal_case_to_snake_case (text):
    result = ""
    for i in text:
        if i.isupper() and result:
            result += "_"
        result += i.lower()
    return result

print (pascal_case_to_snake_case("TestController"))
print (pascal_case_to_snake_case("MoviesAndBooks"))
print (pascal_case_to_snake_case("App7Test"))
print (pascal_case_to_snake_case("1"))