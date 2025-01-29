from manim import *
import math
class Animation(Scene):
    def construct(self):
        

        self.wait()

        # Display the current problem in the top left
        currentProblem = Text("1. (A)").align_on_border(UL)
        self.play(Write(currentProblem))



        # Add positive charge
        positive = VGroup()
        circle = Circle(radius=0.2).set_fill(RED_E, opacity=1)
        circle.set_stroke(RED_A, width=3)
        positive.add(circle)
        positive.add(Text("+").scale(0.5).set_color(RED_A))
        positiveLabel = Text("3.0 nC").scale(0.6)
        positiveLabel.add_updater(lambda mob: mob.next_to(positive, LEFT))
        self.play(Write(positive), Write(positiveLabel))

        # Add vertical axis
        verticalAxis = NumberLine(rotation=math.pi/2,x_range=[0,10,1], tick_size=0.05, length=3)
        verticalAxis.set_z_index(circle.z_index -3)
        verticalAxis.next_to(positive, direction=DOWN, buff=0)
        verticalAxis.shift(DOWN * (verticalAxis.get_end()[1] - circle.get_center()[1]))
        self.play(GrowFromPoint(verticalAxis, positive.get_center()))
        verticalAxisLabel = Text("10 cm",).scale(0.4)
        verticalAxisLabel.add_updater(lambda mob: mob.move_to(verticalAxis.get_center() + LEFT*0.5))
        self.play(Write(verticalAxisLabel))
    
        # Shift up to center and scale
        self.play(verticalAxis.animate.shift(-verticalAxis.get_center()),
        positive.animate.shift(-verticalAxis.get_center()))

        negative = VGroup()
        circle = Circle(radius=0.2).set_fill(BLUE_E, opacity=1)
        circle.set_stroke(BLUE_A, width=3)
        negative.add(circle)
        negative.add(Text("-").scale(0.5).set_color(BLUE_A))
        negative.move_to(verticalAxis.get_start())
        negativeLabel = Text("-6.0 nC").scale(0.6)
        negativeLabel.add_updater(lambda mob: mob.next_to(negative, LEFT))
        self.play(Write(negative), Write(negativeLabel))

        # Add horizontal axis
        horizontalAxis = NumberLine(x_range=[0,5,1], tick_size=0.05, length=3/2)
        horizontalAxis.set_z_index(circle.z_index -3)
        horizontalAxis.shift(positive.get_center() - horizontalAxis.get_start())
        self.play(GrowFromPoint(horizontalAxis, positive.get_center()))
        horizontalLabel = Text("5 cm",).scale(0.4)
        horizontalLabel.add_updater(lambda mob: mob.move_to(horizontalAxis.get_center() + UP*0.5))
        self.play(Write(horizontalLabel))

        # Add point in space
        point = Circle(radius=0.1, color=WHITE,
        fill_color=GREEN, fill_opacity=1).move_to(horizontalAxis.get_end())
        self.play(GrowFromCenter(point))

        # Combine into one object for easy modification
        problemOneModel = VGroup()
        problemOneModel.add(positive, positiveLabel, negative, negativeLabel, point,
        horizontalAxis, horizontalLabel, verticalAxis, verticalAxisLabel)
        self.play(problemOneModel.animate.shift(LEFT * 5))

        # Super position
        superposition = MathTex(r"E_{net}", r"=", r"E_{+}", "+", r"E_{-}").scale(2)
        self.play(Write(superposition))
        self.play(superposition.animate.scale(0.5).align_on_border(UR))


        # Electric feild of point charge
        electricFeild = MathTex(r"E = k\frac{Q}{r^2}", r"\hat{r}").scale(2)
        self.play(Write(electricFeild))
        self.play(electricFeild.animate.scale(0.5).next_to(superposition, DOWN))

        # Highlight positive charge
        charge = SurroundingRectangle(positive)
        text = SurroundingRectangle(superposition[2])
        self.play(Write(charge), Write(text))
        self.play(Unwrite(charge), Unwrite(text))

        # Solve E+
        positiveField = MathTex("E_{+}", "=", r"k", r"\frac{Q}{r^2}", r"\hat{r}")
        indicatorOne = SurroundingRectangle(positiveField[3][0])
        indicatorTwo = SurroundingRectangle(positive)
        self.play(Write(positiveField))
        self.play(Write(indicatorOne), Write(indicatorTwo))
        positiveFieldNext = MathTex("E_{+}", "=", r"k", r"\frac{3 \text{ nC}}{r^2}", r"\hat{r}")
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[3][0:3])),
        TransformMatchingShapes(positiveField, positiveFieldNext))
        
        positiveField = positiveFieldNext
        positiveFieldNext = MathTex("E_{+}", "=", r"k", r"\frac{3 \times 10^{-9} \text{ C}}{r^2}", r"\hat{r}")
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[3][0:7])),
        TransformMatchingShapes(positiveField, positiveFieldNext))

        self.play(Transform(indicatorOne, SurroundingRectangle(positiveField[3][7:9])),
        Transform(indicatorTwo, SurroundingRectangle(horizontalLabel)))

        positiveField = positiveFieldNext
        positiveFieldNext = MathTex("E_{+}", "=", r"k", r"\frac{3 \times 10^{-9} \text{ C}}{(5 \text{ cm})^2}", r"\hat{r}")
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[3][7:13])),
        TransformMatchingShapes(positiveField, positiveFieldNext))

        positiveField = positiveFieldNext
        positiveFieldNext = MathTex("E_{+}", "=", r"k", r"\frac{3 \times 10^{-9} \text{ C}}{0.05^2 \text{ m}^2}", r"\hat{r}")
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[3][7:15])),
        TransformMatchingShapes(positiveField, positiveFieldNext))
        self.play(Unwrite(indicatorOne), Unwrite(indicatorTwo))

        positiveField=positiveFieldNext 
        indicatorOne = SurroundingRectangle(positiveField[2])
        positiveFieldNext = MathTex("E_{+}", "=", r"\frac{1}{4\pi\epsilon_0}", r"\frac{3 \times 10^{-9} \text{ C}}{0.05^2 \text{ m}^2}", r"\hat{r}")
        self.play(Write(indicatorOne))
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[2])),
        TransformMatchingShapes(positiveField, positiveFieldNext))
 
        positiveField=positiveFieldNext 
        positiveFieldNext = MathTex("E_{+}", "=", r"8.99 \times 10^9 \frac{\text{N}\text{m}^2}{\text{C}^2}", r"\frac{3 \times 10^{-9} \text{ C}}{0.05^2 \text{ m}^2}", r"\hat{r}")
        self.play(Transform(indicatorOne, SurroundingRectangle(positiveFieldNext[2])),
        TransformMatchingShapes(positiveField, positiveFieldNext))
        self.play(Unwrite(indicatorOne), Unwrite(indicatorTwo))

        positiveField = positiveFieldNext;
        positiveFieldNext = MathTex("E_{+}", "=", r"8.99 \times 10^9", r"\frac{3 \times 10^{-9} }{0.05^2}", r"\frac{\text{N}}{\text{C}}", r"\hat{r}")
        self.play(TransformMatchingShapes(positiveField, positiveFieldNext))
        self.wait()
         
        # Draw arrow to indicate field induced by positive charge
        arrow = Arrow(start=point.get_center(), end=point.get_center() + RIGHT*2, color=RED)
        arrow.set_length(1).shift(point.get_center() - arrow.get_start())
        self.play(Write(arrow))
        positiveField = positiveFieldNext;
        positiveFieldNext = MathTex("E_{+}", "=", r"8.99 \times 10^9", r"\frac{3 \times 10^{-9} }{0.05^2}", r"\frac{\text{N}}{\text{C}}", r"\hat{i} + 0\hat{j}")
        indicatorOne = SurroundingRectangle(positiveFieldNext[5])
        indicatorTwo= SurroundingRectangle(arrow)
        self.play( Write(indicatorTwo ))
        self.play(TransformMatchingShapes(positiveField, positiveFieldNext), Transform(indicatorTwo, indicatorOne))
        self.play(Unwrite(indicatorOne), Unwrite(indicatorTwo), Unwrite(arrow))
        positiveField = positiveFieldNext

        # Shrink into corner
        self.play(positiveField.animate.next_to(superposition, LEFT).scale(0.5))

        # Now lets do the negative field
        indicatorOne = SurroundingRectangle(negative)
        indicatorTwo = SurroundingRectangle(superposition[4])
        self.play(Write(indicatorOne), Write(indicatorTwo))
        self.play(Unwrite(indicatorOne), Unwrite(indicatorTwo))
        
        negativeField = MathTex("E_{-}", "=", r"k", r"\frac{Q}{r^2}", r"\hat{r}")
        self.play(TransformFromCopy(electricFeild, negativeField))
        indicatorOne = SurroundingRectangle(negativeLabel)
        indicatorTwo = SurroundingRectangle(negativeField[3][0])
        self.play(Write(indicatorOne), Write(indicatorTwo))
        negativeFieldNext = MathTex("E_{-}", "=", r"k", r"\frac{-6 \text{ nC}}{r^2}", r"\hat{r}")
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext),Transform(indicatorTwo, SurroundingRectangle(negativeFieldNext[3][0:4])))
        negativeField = negativeFieldNext

        negativeFieldNext = MathTex("E_{-}", "=", r"k", r"\frac{-6 \times 10^{-9} \text{ C}}{r^2}", r"\hat{r}")
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext), Transform(indicatorTwo, SurroundingRectangle(negativeFieldNext[3][0:8])))
        self.play(Unwrite(indicatorOne), Unwrite(indicatorTwo))
        negativeField = negativeFieldNext
        line = Line(start=negative.get_center(), end=point.get_center()).set_color(BLUE).set_z_index(positive.z_index - 1)
        lineLabel = MathTex(r"r = \sqrt{x^2 + y^2}").scale(0.6).set_color(BLUE)
        lineLabel.next_to(line, RIGHT, buff=-1.3)
        indicatorOne = SurroundingRectangle(lineLabel)
        lineLabel.rotate(line.get_angle())
        indicatorOne.rotate(line.get_angle())
        indicatorTwo = SurroundingRectangle(negativeField[3][9:11])
        self.play(Write(line), Write(lineLabel), Write(indicatorTwo), Write(indicatorOne))

        lineLabelNext = MathTex(r"r = \sqrt{0.05^2 + 0.1^2} \text{ m}", r"\hat{r}").scale(0.6).set_color(BLUE).move_to(lineLabel)
        indicatorOneNext = SurroundingRectangle(lineLabelNext)
        lineLabelNext.rotate(line.get_angle())
        indicatorOneNext.rotate(line.get_angle())
        self.play(Transform(indicatorOne, indicatorOneNext), Transform(lineLabel, lineLabelNext))
        negativeFieldNext = MathTex("E_{-}", "=", r"k", r"\frac{-6 \times 10^{-9} \text{ C}}{0.05^2 + 0.1^2 \text{ m}}", r"\hat{r}")
        curvedArrow = CurvedArrow(start_point=lineLabel.get_center() + RIGHT*0.4, end_point=negativeField[3][9].get_center() + DOWN*0.3)
        self.play(Write(curvedArrow))
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext), 
        Transform(indicatorTwo, SurroundingRectangle(negativeFieldNext[3][9:20])))
        self.wait()
        self.play(Unwrite(curvedArrow), Unwrite(indicatorOne), Unwrite(indicatorTwo), Unwrite(line), Unwrite(lineLabel))
        negativeField = negativeFieldNext
        indicatorOne = SurroundingRectangle(negativeField[2])
        self.play(Write(indicatorOne))
        curvedArrow = CurvedArrow(start_point = positiveField[2].get_center() + DOWN *0.3, end_point = negativeField[2].get_center() + UP *0.3)
        self.play(Write(curvedArrow))
        negativeFieldNext = MathTex("E_{-}", "=", r"8.99 \times 10^9 \frac{\text{N}\text{m}^2}{\text{C}^2}", r"\frac{-6 \times 10^{-9} \text{ C}}{0.05^2 + 0.1^2 \text{ m}}", r"\hat{r}")
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext), 
        Transform(indicatorOne, SurroundingRectangle(negativeFieldNext[2])))
        self.wait()
        self.play(Unwrite(curvedArrow), Unwrite(indicatorOne), Unwrite(indicatorTwo))
        negativeField = negativeFieldNext
        units = VGroup()
        units.add(SurroundingRectangle(negativeField[2][7:]), SurroundingRectangle(negativeField[3][7]),
        SurroundingRectangle(negativeField[3][19]))
        self.play(Write(units))
        negativeFieldNext = MathTex("E_{-}", "=", r"8.99 \times 10^9", r"\frac{-6 \times 10^{-9} }{0.05^2 + 0.1^2 }", r"\frac{\text{N}}{\text{C}}", r"\hat{r}")
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext), 
        Transform(units, SurroundingRectangle(negativeFieldNext[4]))) 
        self.wait()
        negativeField = negativeFieldNext
        self.play(Unwrite(units))
        # Solve for r hat
        arrow = Arrow(start=negative.get_center(), end=point.get_center())
        arrow.set_length(1).set_color(BLUE).move_to(point.get_center()).shift(point.get_center() - arrow.get_start())
        arrowLabel = MathTex(r"-\hat{r}").next_to(arrow, RIGHT).set_color(BLUE)
        self.play(Write(arrow), Write(arrowLabel))
        line1 = Line(start=negative.get_center(), end = point.get_center())
        line2 = Line(start=negative.get_center(), end = positive.get_center())
        angle = Angle(line1, line2, radius=1).set_color(BLUE)
        angleLabel = MathTex(r"\theta").next_to(angle, UP)
        dashed = DashedLine(start = negative.get_center(), end= point.get_center())
        self.play(Write(angle), Write(angleLabel), Write(dashed))
        self.wait()

        arrowLabelNext = MathTex(r"\hat{r} = sin{(\theta)} \hat{i} + cos{(\theta)} \hat{j}").next_to(arrow, RIGHT).set_color(BLUE).scale(0.8)
        self.play(TransformMatchingShapes(arrowLabel, arrowLabelNext))
        self.wait()
        arrowLabel = arrowLabelNext
        arrowLabelNext = MathTex(r"\hat{r} = \frac{0.05}{\sqrt{0.1^2 + 0.05^2}} \hat{i} + \frac{0.1}{\sqrt{0.05^2 + 0.01^2}} \hat{j}").scale(0.8).next_to(arrow, RIGHT).set_color(BLUE)
        self.play(TransformMatchingShapes(arrowLabel, arrowLabelNext))
        self.wait()
        arrowLabel = arrowLabelNext

        negativeFieldNext = MathTex("E_{-}", "=", r"8.99 \times 10^9", r"\frac{-6 \times 10^{-9} }{0.05^2 + 0.1^2 }", r"\frac{\text{N}}{\text{C}}", r"(\frac{0.05}{\sqrt{0.1^2 + 0.05^2}} \hat{i} + \frac{0.1}{\sqrt{0.05^2 + 0.01^2}} \hat{j})").scale(0.6).shift(RIGHT)
        self.play(TransformMatchingShapes(negativeField, negativeFieldNext))
        self.wait()
        negativeField = negativeFieldNext
        self.play(Unwrite(arrowLabel),Unwrite(arrow),Unwrite(angle), Unwrite(angleLabel), Unwrite(dashed))
        self.play(negativeField.animate.center().shift(RIGHT + DOWN*2).scale(1.3))
        self.play(positiveField.animate.scale(2).next_to(negativeField, UP))

        negativeFieldNext = MathTex("E_{-}", "=", r"(-1929.816\hat{i} - 3859.632 \hat{j})", r"\frac{\text{N}}{\text{C}}").move_to(negativeField)
        positiveFieldNext = MathTex("E_{+}", "=", r"(10788\hat{i} + 0\hat{j})", r"\frac{\text{N}}{\text{C}}").move_to(positiveField)

        self.play(TransformMatchingShapes(negativeField, negativeFieldNext),
        TransformMatchingShapes(positiveField, positiveFieldNext))
        self.wait()
        negativeField = negativeFieldNext
        positiveField = positiveFieldNext
        group = VGroup()
        group.add(negativeField)
        group.add(positiveField)
        group.add(superposition)
        superCombined = MathTex("E_{net}", "=", r"[(10788\hat{i} + 0\hat{j}) +(-1929.816\hat{i} - 3859.632 \hat{j})]", r"\frac{\text{N}}{\text{C}}").scale(0.7)
        superCombinedNext = MathTex("E_{net}", "=", r"(8858.184\hat{i} - 3859.632\hat{j}) ", r"\frac{\text{N}}{\text{C}}").scale(0.7)
        self.play(TransformMatchingShapes(group, superCombined))
        self.wait()
        group = superCombined
        self.play(TransformMatchingShapes(group, superCombinedNext))
        self.wait()
        group = superCombinedNext
        superCombinedNext = MathTex("\|E_{net}\|", "=", r"\sqrt{(8858.184\hat{i})^2 + (-3859.632\hat{j})^2} ", r"\frac{\text{N}}{\text{C}}").scale(0.7)

        self.play(TransformMatchingShapes(group, superCombinedNext))
        group = superCombinedNext

        superCombinedNext = MathTex("\|E_{net}\|", "=", r"9662.51", r"\frac{\text{N}}{\text{C}}").scale(0.7)
        self.wait()
        self.play(TransformMatchingShapes(group, superCombinedNext))
        group = superCombinedNext
        self.wait() 
        self.play(Flash(currentProblem))
        currentProblemNext = Text("1. (B)").align_on_border(UL)
        self.play(TransformMatchingShapes(currentProblem, currentProblemNext))
        currentProblem=currentProblemNext

        self.wait()

        superCombinedNext = MathTex("E_{net}", "=", r"(8858.184\hat{i} - 3859.632\hat{j}) ", r"\frac{\text{N}}{\text{C}}").scale(0.7)
        self.play(TransformMatchingShapes(group, superCombinedNext.shift(UP * 2)))
        group = superCombinedNext

        angle = MathTex(r"\text{Angle of }", r"E_{net}", "=", r"\arctan{( \frac{ \hat{j} }{ \hat{i} } )}")
        self.play(Write(angle))
        
        angleNext = MathTex(r"\text{Angle of }", r"E_{net}", "=", r"\arctan{(\frac{-3859.632}{8858.184 })}")
        self.play(TransformMatchingShapes(angle, angleNext))
        angle = angleNext

        angleNext = MathTex(r"\text{Angle of }", r"E_{net}", "=", r"-23.54^o \text{ CC}")
        self.wait()
        self.play(TransformMatchingShapes(angle, angleNext))
        angle = angleNext
        self.wait()
        angleNext = MathTex(r"\text{Angle of }", r"E_{net}", "=", r"23.54^o \text{ CW}")
        self.play(TransformMatchingShapes(angle, angleNext))
        angle = angleNext
        self.play(Unwrite(angle))
        rect = Square().scale(20).set_color(WHITE)
        self.play(Write(rect))
        self.wait()
with tempconfig({"quality": "low_quality", "preview": True}):
    scene = Animation()
    scene.render()
