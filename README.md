<h1>Mass Website Keyword Scanner</h1>

<p>
  <strong>PyWKS is a Python script for a mass website keyword scanner.</strong><br>
  It allows you to check multiple websites for the presence of a specific keyword concurrently using multiple threads.
</p>

<h2>Requirements</h2>

<p>
  Before running the script, ensure you have the following installed:
</p>

<ul>
  <li>Python 3</li>
  <li>Requests library (<code>pip install requests</code>)</li>
  <li>Colorama library (<code>pip install colorama</code>)</li>
  <li>Urllib3 library (<code>pip install urllib3</code>)</li>
</ul>

<h2>How to Use</h2>

<img src="https://github.com/im-hanzou/PyWKS/blob/main/pywks.JPG"><br>
<ol>
  <li>Clone or download the script.</li>
  <li>Open a terminal or command prompt in the directory containing the script.</li>
  <li>Run the script using the following command:</li>
</ol>

<pre><code>python script.py</code></pre>

<h2>Input Parameters</h2>

<ul>
  <li><strong>List:</strong> Path to the file containing a list of URLs to check (one URL per line).</li>
  <li><strong>Insert Keyword:</strong> The keyword you want to search for on the websites.</li>
  <li><strong>Threads:</strong> Number of threads to use for concurrent scanning.</li>
</ul>

<h2>Example</h2>

<pre><code>List: websites.txt
Insert Keyword: example
Threads: 5
</code></pre>

<h2>Result</h2>

<p>
  The script will scan each URL in the <code>websites.txt</code> file for the specified keyword (<code>example</code> in this case).
  The output will show whether the keyword is found or not on each website.
  Found URLs will be saved in <code>results.txt</code> file.
</p>

<h2>Note</h2>

<ul>
  <li>Make sure the URLs are listed in the <code>websites.txt</code> file.</li>
  <li>The script may take some time to complete depending on the number of websites and threads used.</li>
</ul>

<h2>Disclaimer</h2>

<p>
  <em>This script is intended for educational and ethical purposes only. The author is not responsible for any misuse or illegal activities. Use at your own risk.</em>
</p>

<hr>

<p>
  <em>Coded By <a href="https://github.com/im-hanzou/">im-hanzou</a> /w L</em>
</p>
