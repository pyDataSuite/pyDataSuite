import asyncio
import tkinter as tk

loop = asyncio.get_event_loop()

async def async_main( window: tk.Tk ):
    while True:
        try:
            window.update()
            await asyncio.sleep( 0.01 )
        except tk.TclError:
            exit( 0 )

def asyncloop( window: tk.Tk ):
    try:
        loop.run_until_complete( async_main( window ) )
    except KeyboardInterrupt:
        exit( 0 )