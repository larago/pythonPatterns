# First to look at main() func

def main():

    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory())
    txtDiagram.save(textFilename)

# First to create two files, first is pure text, second one is SVG
# And what create_diagram() looks like inside?

def create_diagram(factory):

    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

# After go through how to use factory, let's look at factory itself.
# Below was a pure text factory

class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill='white', stroke='black'):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y ,text, fontsize)

class SvgDigramFactory:

    def make_diagram(self, width, height):
        return SvgDigram(width, height)

    def make_rectangle(self, x, y, width, height, fill='white', stroke='black'):
        return SvgRectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)

# They are very simillar but essential differences between them is they return different objects
# One is Diagram object, another one is SvgDiagram
# Later we would see even though is seems almost exactly same
# but details of construnction is very different, that's why we can't mix them together

class Text:

    def __inuit__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [List(text)]

#Those are all codes of class Text(), we don't concerned with fontsize causes it's pure text

class Diagram:

    def add(self, component):
        for y, row in enmuerate(component.rows):
            for x, char in enmuerate(row):
                self.diagram[y + component.y][x + component.x]

# all instants that class SvgText() reply on listed below:

SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family= "sans-serif" font-size="{fontsize}">{text}</text>"""

SVG_SCALE = 20

class SvgText:

    def __init__(self, x, y, text, fontsize):
        x *= SVG_SCALE
        y *= SVG_SCALE
        fontsize *= SVG_SCALE // 10
        self.svg = SVG_TEXT.format(**locals())

class SvgDiagram:

    def add(self,component):
        self.diagram.append(component.svg)

#All presents above shows the modle of factory, but they are not really necessary
#Because they have no status, so actually no need to create class
#Besides, a lot of codes repeat, it's not that good