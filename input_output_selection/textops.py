text="presbyterian"
other="BYTE"

print text,text.upper()

if text.find(other)>=0:
    print "%s is in %s"%(other,text)
else:
    print "%s is NOT in %s"%(other,text)

if text.upper().find(other.upper())>=0:
    print "%s is in %s (ignoring case)"%(other,text)
else:
    print "%s is NOT in %s (ignoring case)"%(other,text)
