from turtle import*

pencil = Turtle()
colors = ["red" , "blue", "green", "yellow", "orange", "grey"]

for i in range(6):
	pencil.color(colors[i])
	pencil.width(5)
	pencil.fd(100)
	pencil.right(60)
done()
