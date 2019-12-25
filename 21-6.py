import os
>>> os.path.basename(os.path.dirname('/foo/bar/baz/file'))
'baz'
>>> os.path.basename(os.path.dirname('/file'))