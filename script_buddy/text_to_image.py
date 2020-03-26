import PIL
from PIL import Image, ImageDraw

img = Image.new('RGB', (300, 400), color = 'white')

d = ImageDraw.Draw(img)

string = """
 JACK


                        (BEAT)
          What's wrong with that? It's a
          good movie! You know, I really
          don't know. You know, I like
          some of the stuff in it.


                         CUT TO:


          INT.  JACK AND DOLORES' ROOM/BEDROOM - MOMENTS LATER

          CUT BACK to JACK, in his robe. He's laying a
          blanket against his head. He lies still, his face in
          the blanket.


                         JACK
          I'm all right.


                         DOLORES
          Yeah, you're okay.


                         JACK
          I'm all right, too. But
          sometimes when I think about a
          dream, it's all a bunch of stuff
         
          DOLORES looks into his eyes for a long
          beat. Then he gets up, kisses JACK.


                         DOLORES (CONT'D)
          It can be an eye opener,
          you know? I can tell.


                         JACK


                         (BEAT)
          What's the difference?


                         CUT TO:


          INT.  JACK AND DOLORES' ROOM/BEDROOM - LATE AFTERNOON

         JACK looks at his hand in his robe. He's still
         sleeping. CUT BACK to:


         CUT TO:


         INT.  CASSADY'S APARTMENT - MOMENTS LATER

        JACK is on the sofa, looking at the television.


                     JACK
         What you told me.


                    CASSADY
        What you told me, what you
        told me...


                     (ON TV)
        What are you telling me, I can't
        believe this...


                   JACK
         Yeah. I told you... I told
        you that the movies I do
        get are for girls who
        don't know how to act...
"""
d.text((5,5), string, fill=(0,0,0))

img.save('pil_red.png')
