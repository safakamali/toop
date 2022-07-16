from Resources.appresorces import Command

@Command("sayhello")
def sayhello(args):
    print(f"Hello {args[0]}")