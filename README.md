# Light novel translator using gemini

--------------

## Environment
 - Linux( or BSD, not tested yet)
 - python 3.11 ( lower version may also support)
 - Windows is not supported(may can run now, but no support in the future)

## Usage
 - Put the api key of google gemini in `config.ini` (just replace the `???`)
 - Get the api key in `ai.google.dev`
 - `get_ncode.py ${id}` to crawl ncode novels
 - `get_kakuyomu.py ${id}` to crawl kakuyomu novels
 - `auto_translate_gemini.py ${id} ${range_start} ${optional:range_end}`
 - `bin/translate-ncode` and `bin/translate-kakuyomu` are scripts to crawl and translate  
## Store location
`./novel/{novel_id}.cn/`

## LICENSE

Released under the MIT license


  
