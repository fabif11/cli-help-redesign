from pydoc import cli
import click

@click.command()
@click.option("--helplist", "-hl", is_flag=True, show_default=True, default=False, help="Show commands help as a list")
@click.option("--helpgroup", "-hg", is_flag=True, show_default=True, default=False, help="Show commands help as a group")
def queb(helplist, helpgroup): 

    if helpgroup:
        print('''
        Usage:
        program + command + option + argument
        program + n*argument
        program + optional argument
        …

        Options:
        SYSTEM
            -h --help   
            -clr {True, False}, --clear_terminal {True, False}
            -f FILE, --file FILE
            -p PATH, --path PATH    
        SPACE
            -col COLUMNS [COLUMNS ...], --columns COLUMNS [COLUMNS ...]
            -d DELIMITER, --delimiter DELIMITER
        LOOK
            -m MARKER, --marker MARKER 
            -t TITLE, --title TITLE    
            -xl XLABEL, --xlabel XLABEL    
            -yl YLABEL, --ylabel YLABEL    
            -c COLOR, --color COLOR
            -g {True,False}, --grid {True,False}
        STATUS
            -s SLEEP, --sleep SLEEP
            '''
        )
    if helplist:
        print('''
        Usage:
        program + command + option + argument
        program + n*argument
        program + optional argument
        …

        Options:
        -h --help   
        -clr {True, False}, --clear_terminal {True, False}
        -f FILE, --file FILE
        -p PATH, --path PATH    
        -col COLUMNS [COLUMNS ...], --columns COLUMNS [COLUMNS ...]
        -d DELIMITER, --delimiter DELIMITER
        -m MARKER, --marker MARKER 
        -t TITLE, --title TITLE    
        -xl XLABEL, --xlabel XLABEL    
        -yl YLABEL, --ylabel YLABEL    
        -c COLOR, --color COLOR
        -g {True,False}, --grid {True,False}
        -s SLEEP, --sleep SLEEP
    ''')
