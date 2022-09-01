from pydoc import cli
import click

@click.command()
@click.option('--n', default=1, show_default=True)
@click.option("--helplist", is_flag=True, show_default=True, default=False, help="Greet the world.")
@click.option("--helpgroup", is_flag=True, show_default=True, default=True, help="Add a thematic break")
#@click.option('--helplist', '-hl', is_flag=True)
#@click.option('--helpgroup', '-hg', is_flag=True)
def queb(n, helplist, helpgroup): 

    if helplist:
        print('''
        Usage:
            program plot [options] <argument>

        Options:
        SYSTEM
            -h --help   
            -p PATH, --path PATH    
        TEXT
            -t TITLE, --title TITLE    
            -xl XLABEL, --xlabel XLABEL    
            -yl YLABEL, --ylabel YLABEL    
        LOOK
            -c COLOR, --color COLOR     
            -m MARKER, --marker MARKER      
        STATUS
            -s SLEEP, --sleep SLEEP
            '''
        )
    if helpgroup:
        print("ciao")
