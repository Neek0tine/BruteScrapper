


<img src="https://github.com/Neek0tine/Scrapper/blob/main/assets/1-01.jpg" alt="DaNg" width="800"/><br>

# What is it?
**BruteScrapper** is a joint repository of four college students whose goal is just one: **be able gather data from websites**. The ability to gather data from online websites are really strict nowadays. Irresponsible webscrappers tend to let their program run unlimitedly which causes a level of traffic comparable to DDoS attack, therefore websites tend to use bot-prevention measures to just deny webscrappers as a whole. Usually, this kind of case is really common and site admin provides APIs and Endpoints in where webscrappers can gather info regulatedly. But in some case where they just block bots and is not planning to give any APIs, scrapprers are stuck with no solution. This module is a solution to exact problem.

While this module sounds selfish and inconsiderate, this method ensures the livelihood of the website scrapped for the speed of this module is severely reduced because of the natural limitations of peripheral manipulation. This module is more of a browser automation and less of a tool that specializes in web browsing such as `selenium` or tool that requests data such as `urllib` or `requests`

# Why did I make this?
You can only annoy someone so much until they snap and decided to create something like this. The idea behind this 
module is that we're using something similar as AutoHotKey, in this case PyAutoGUI. Then we just made a bunch of sequences
and arrange them into classes and functions that is similar to requests or urllib class structure for easier use.

Text gathering is done by using clipboard module, since PyTesseract is a heavy library and generally a hassle to use. 
The text gathered is mostly from page source that has been soup'd or a simple select all texts on the site, I surely am will make
a function that does exactly like that but in a more controlled way.

"How about nested links?" You ask? Simple. PyAutoGUI has this amazing feature that lets you get a coordinate of an image 
given that you give PyAutoGUI target image. Target image is gathered easily by using something as simple as snipping tool.

# Usage

### PIP
To install using pip, simply type this command:<br>
`pip install git+https://github.com/Neek0tine/BruteScrapperl.git@main`

### Examples
<img src="https://github.com/Neek0tine/Scrapper/blob/main/assets/examples 2.png" alt="DaNg" width="800"/><br>

## End-User License Agreement
As per the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Authors


* [**Miaw** ](https://github.com/ricardo-bdg)
* [**SleepyCats**](https://github.com/FluffHound)
* [**Neek0tine**](https://github.com/Neek0tine)


## Contributing

Pull requests are welcome. For major changes, how-to, and in-depth explanation, please contact one of the authors.
## License
![PyPI - License](https://img.shields.io/pypi/l/PyCl)
<br>
This project is licensed under MIT License - see the [LICENSE](https://github.com/Neek0tine/BruteScrapper/blob/main/LICENSE) file for details
