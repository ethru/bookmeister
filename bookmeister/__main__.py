"""#### Main

Contain `main` function which create application GUI and set its size. Module
`sys` is needed to specify which platform is used and adjust application width.


#### License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from sys import platform

from bookmeister.gui import Gui


def main():
    """Set GUI width according to used platform and run it."""
    width = '450' if platform == 'win32' else '600'
    Gui('Bookstore Manager', f'{width}x470').mainloop()


if __name__ == '__main__':
    main()
