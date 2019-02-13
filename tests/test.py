##This is my funcy ATestClass.
#
# I have no clue, what to do with it.
#
#  \xrefitem KEY "heading" "list title" "the class"
class ATestClass:
    ##And this is the only method.
    #
    #  It prints something.
    #  \test where is my little testy?
    #  \xrefitem KEY "heading" "list title" "the text"
    def test_function(self):
        print("It's me")

    ## \xrefitem KEY "heading" "list title" "the text 2"
    def test_function_2(self):
        print("It's me")

## \addtogroup GROUP_B Group B
#  This is class B
class BTestClass:
    ## \addtogroup GROUP_B
    #  \xrefitem KUH "case" "GROUP_B" the text for B2 
    def test_function(self):
        print("It's me")

    ## \addtogroup GROUP_B
    #  \xrefitem KUH "case" "GROUP_B" the text 2 for B2
    def test_function_2(self):
        print("It's me")

## \addtogroup GROUP_C Group C
#  This is class C
class CTestClass:
    ## \addtogroup GROUP_C
    #  \xrefitem KUH "case" "GROUP_C" the text for C2 
    def test_function(self):
        print("It's me")

    ## \addtogroup GROUP_C
    #  \xrefitem KUH "case" "GROUP_C" the text 2 for C2
    def test_function_2(self):
        print("It's me")

if __name__ == "__main__":
    a = ATestClass()
    a.test_function()
