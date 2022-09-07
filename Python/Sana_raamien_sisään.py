sana = input("Sana: ")
korkeus = 3
raamit = ["*"+(" "*len(sana))+"*"]*korkeus
raamit[0] = raamit[-1] = "*" * (len(sana)+2)
raamit[korkeus//2] = f"*{sana}*"
print("\n".join(raamit))
