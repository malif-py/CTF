from os import chdir

main_txt = open('result (copy).svg')
lines = main_txt.readlines()
chdir('Plethora')
for i in range(len(lines)):
    if lines[i].strip()[:5] == '<path':
        main = '<svg width="10in" height="10in" viewBox="0 0 3000 3000" version="1.1" id="missing-coordinates">\
<g id="flag">'
        con = lines[i]
        end = '    </g>\
</svg>'
        new = open(f"{i}.svg", 'w')
        new.write(main)
        new.write(con)
        new.write(end)