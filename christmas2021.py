import threading
#
import puzzle_functions
from importlib import reload
#from systemtest import *
    
def main(red_led,lcd_screen,switches,buttons,a_combo,b_combo):
    from luma.core.render import canvas
    from time import time, sleep, localtime
    
    switch_1 = switches[0]
    switch_2 = switches[1]
    switch_3 = switches[2]
    switch_4 = switches[3]
    switch_5 = switches[4]
    switch_6 = switches[5]
    switch_7 = switches[6]
    switch_8 = switches[7]
    switch_9 = switches[8]
    
    yellow_button = buttons[0]
    green_button  = buttons[1]
    blue_button   = buttons[2]
    black_button  = buttons[3]
    red_button    = buttons[4]
    white_button  = buttons[5]
    
    a_right  = a_combo[0]
    a_left   = a_combo[1]
    a_button = a_combo[2]
    b_right  = b_combo[0]
    b_left   = b_combo[1]
    b_button = b_combo[2]
    
    def lcd_text(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 10), text, fill="white")

    def lcd_text_4line(text):
        with canvas(lcd_screen) as draw:
            draw.rectangle(lcd_screen.bounding_box, outline="white", fill="black")
            draw.text((10, 5), text, fill="white")

    # def system_on():
        # lcd_text('System Loading\n\n  please wait')
        # red_led.scroll('ON             ON            ON')
        # lcd_text_4line('WELCOME!\nauthenticate\nby entering toggle\nswitch sequence')

    # switch_1.when_pressed = system_on

    # dropping system off until we can get the whole script to start form beginning on restart
    # def system_off():
        # lcd_text('System Shutdown')
        # red_led.scroll('off')
        # lcd_screen.clear()

    # switch_1.when_released = system_off
    switch_1.wait_for_press()

    lcd_text('System Loading\n\n  please wait')
    red_led.scroll('ON             ON            ON')
    lcd_text_4line('WELCOME!\nauthenticate\nby entering toggle\nswitch sequence')

    switch_up_text = ['skip this switch','blitzen','comet','cupid','dancer','dasher','donner','prancer','vixen']
    switch_down_text = ['skip this switch','','','','','','','','']
    switch_sequence = ['6 up','5 up','8 up','9 up','3 up','4 up','7 up','2 up']

    #puzzle_functions = reload(puzzle_functions)
    switch_combo = puzzle_functions.switch_combo
    switch_combo(red_led,switches,switch_sequence,switch_up_text,switch_down_text,'Correct')


    options =          ["         Elf         ","      Reindeer       ","        Tree         "]
    option_responces = ["    you have\n    Selected\n      Elf","    you have\n    Selected\n    Reindeer","    you have\n    Selected\n      Tree"]
    title_rows = [" Select Multi-factor ","authentication method","(use left nob & push)"]



    #puzzle_functions = reload(puzzle_functions)
    rotate_lcd_multiselect = puzzle_functions.rotate_lcd_multiselect
    multiselected = rotate_lcd_multiselect(lcd_screen,a_combo,options,option_responces,title_rows)
    sleep(1)
    if multiselected == 1:
        lcd_text("Check roof/yard\nfor authentication\npackage")
    else:
        lcd_text("Check for present\nTo: Gladys\nFrom:MultiAuthServer")

    sleep(20)
    lcd_text("Use pushbuttons\nto enter multifactor\nauthentication code")

    #puzzle_functions = reload(puzzle_functions)
    pushbutton_sequence = puzzle_functions.pushbutton_sequence
    pushbutton_sequence(lcd_screen,buttons,["white","red","green","yellow","yellow","blue"])
    sleep(5)
    lcd_text("Last login >90 days\nanswer 3 security\nquestions correctly")
    sleep(10)


    security_questions =  [[["   At Jesus's birth  ","who was the governor ","     of Syria?       "],["      Zechariah      ","       Gabriel       ","      Quirinius      ","   Caesar Augustus   ","        Herod        "],["No, Zechariah was\n married to Mary's\ncousin Elisabeth","No, Gabriel was\nthe angel who\nvisited Mary","Yes, Quirinius\nwas the governor\nof Syria","No, Ceasar Agustus\nwas the emperor of\nRome at the time","No, Herod was the\nKing of Judea, but\na puppet of Rome"],[False,False,True,False,False]],[["       How many      ","       wise men      ","     were there?     "],["         One         ","         Two         ","        Three        ","       Several       ","        Twelve       ","     No one knows    "],["In Matthew 3 gifts\n are named but not\nthe # of wise men","In Matthew 3 gifts\n are named but not\nthe # of wise men","In Matthew 3 gifts\n are named but not\nthe # of wise men","In Matthew 3 gifts\n are named but not\nthe # of wise men","In Matthew 3 gifts\n are named but not\nthe # of wise men","In Matthew 3 gifts\n are named but not\nthe # of wise men"],[False,False,False,False,False,True]],[["    Why were Mary    ","    and Joseph in    ","      Bethlehem      "],[" Visit Mary's Family ","Register for a census","   They lived there  ","      Vacation!      ","No room in Jerusalem "],["Caesar issued a\ndecree that a\ncensus be taken","Caesar issued a\ndecree that a\ncensus be taken","Caesar issued a\ndecree that a\ncensus be taken","Caesar issued a\ndecree that a\ncensus be taken","Caesar issued a\ndecree that a\ncensus be taken",],[False,True,False,False,False]],[["Who held infant Jesus","in the temple courts ","  and praised God?   "],["         Mary        ","        Joseph       ","        Simeon       "," Anna the prophetess "],["Luke 2:28 ,Simeon\ntook him in his arms\nand praised God","Luke 2:28 ,Simeon\ntook him in his arms\nand praised God","Luke 2:28 ,Simeon\ntook him in his arms\nand praised God","Luke 2:28 ,Simeon\ntook him in his arms\nand praised God"],[False,False,True,False]],[["What did the Angel of","the Lord say to the ","    Shepherds?      "],["  Do not be afraid   ""I bring you good news"," Savior has been born","You will find a baby "],["\nCorrect\n","\nCorrect\n","\nCorrect\n","\nCorrect\n"],[True,True,True,True]],[["   What was Jesus's  ","    mother's name?   ","                     "],["         Mary        "],["\nCorrect\n"],[True]],[["    What was God's   ","    Christmas gift   ","       for us?       "],["        Jesus        "],["\nCorrect\n"],[True]]]

    total_correct = 0

    for i in range(7):
        if total_correct < 3:
            answer_index = rotate_lcd_multiselect(lcd_screen,a_combo,security_questions[i][1],security_questions[i][2],security_questions[i][0])
            print("answer was")
            print(security_questions[i][3][answer_index])
            total_correct = total_correct + security_questions[i][3][answer_index]
            print("total correct")
            print(total_correct)
            sleep(4)
            lcd_text("you have "+str(total_correct)+"\ntotal correct\nyou need 3")
            sleep(4)



    lcd_text("Welcome Gladys\nwho whants what\nfor Christmas?")
    sleep(5)

    kids = ["Jonny","Timmy","Nellie","Susie","Kelly"]
    gifts = ["bicycle","book","doll","skates","sweater"]
    gift_correct_order = ['skates', 'sweater', 'book', 'doll', 'bicycle']



    def final_order_selection():
        selected_gift_list = []
        for kid in kids:
            selected_gift = gifts[rotate_lcd_multiselect(lcd_screen,a_combo,gifts,['','','','',''],["    For Christmas    ","     this year       ",kid+" would like"])]
            selected_gift_list.append(selected_gift)
        lcd_text("Processing Order\n\n  Please Wait")
        sleep(5)
        if selected_gift_list == gift_correct_order:
            lcd_text("Order Complete\nOrder ID: js54Qv9\nMerry Christmas!")
            sleep(60)
        else:
            lcd_text_4line("Order Submission\nInconsistent\nwith records\nPlease try again")
            sleep(10)
            final_order_selection()

    final_order_selection()


if __name__ == "__main__":
    from systemtest import *
    main(red_led,lcd_screen,switches,buttons,a_combo,b_combo)
