print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")

class Kangaroo:
    def _init_(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def _str_(self):
        result = "Kangaroo pouch contents:\n"
        for item in self.pouch_contents:
            result += f"  {str(item)}\n"
        return result.strip()


def main():
    kanga = Kangaroo()
    roo = Kangaroo()

    kanga.put_in_pouch("wallet")
    kanga.put_in_pouch("keys")
    kanga.put_in_pouch(roo)

    print("Kanga:")
    print(kanga)
    print("\nRoo:")
    print(roo)


if _name_ == "_main_":
    main()
