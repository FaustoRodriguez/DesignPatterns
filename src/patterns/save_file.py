def create_file(content: str,filename:str):
    with open(filename, "w") as file:
        file.write(content)

#Using the Single responsability principle we're relieving the report componets of doing another job and we're also reutilizing one component for both
