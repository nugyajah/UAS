import ascii_magic
output = ascii_magic.from_image_file("mobil.jpg", columns=50,char="#")
ascii_magic.to_terminal(output)
