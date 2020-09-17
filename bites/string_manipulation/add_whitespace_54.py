import re
INDENTS = 4
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
                        To be, or not to be, that is the question:
                            Whether 'tis nobler in the mind to suffer
                        The slings and arrows of outrageous fortune,
                            Or to take Arms against a Sea of troubles,
                        """
def print_hanging_indents(poem):
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines()
                 if line.strip()]
        print(lines[0])
        for line in lines[1:]:
            print(' ' * INDENTS + line)
            
print_hanging_indents(shakespeare_unformatted)