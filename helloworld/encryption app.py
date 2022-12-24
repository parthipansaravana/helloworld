def cryption(sentence):
    encryption=""
    for e in sentence:
        if e in "Aa":
            encryption=encryption+"1"
        elif e in "Bb":
            encryption = encryption + "2"
        elif e in "Cc":
            encryption=encryption+"3"
        elif e in "Dd":
            encryption=encryption+"4"
        elif e in "Ee":
            encryption=encryption+"5"
        elif e in "Ff":
            encryption=encryption+"6"
        elif e in "Gg":
            encryption=encryption+"7"
        elif e in "Hh":
            encryption=encryption+"8"
        elif e in "Ii":
            encryption=encryption+"9"
        elif e in "Jj":
            encryption=encryption+"!"
        elif e in "Kk":
            encryption=encryption+"@"
        elif e in "Ll":
            encryption=encryption+"#"
        elif e in "Mm":
            encryption=encryption+"$"
        elif e in "Nn":
            encryption=encryption+"%"
        elif e in "Oo":
            encryption=encryption+"^"
        elif e in "Pp":
            encryption=encryption+"&"
        elif e in "Qq":
            encryption=encryption+"*"
        elif e in "Rr":
            encryption=encryption+"("
        elif e in "Ss":
            encryption=encryption+")"
        elif e in "Tt":
            encryption=encryption+"{"
        elif e in "Uu":
            encryption=encryption+"}"
        elif e in "Vv":
            encryption=encryption+"["
        elif e in "Ww":
            encryption=encryption+"]"
        elif e in "Xx":
            encryption=encryption+":"
        elif e in "Yy":
            encryption=encryption+"<"
        elif e in "Zz":
            encryption=encryption+">"
        else:
            encryption=encryption+e

    return encryption
print(cryption(input("enter text need to encrypt:")))