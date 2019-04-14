# ngraph.louvain.native

Similar to [ngraph.louvain](https://github.com/anvaka/ngraph.louvain), this module
detects clusters in a graph using the [Louvain Method](https://en.wikipedia.org/wiki/Louvain_Modularity).

The major difference here, is that this is a native node module, with C++ bindings, so that computation
happens much faster. 

Alas, this means this module can only work in node.js environment.

If you need pure javascript implementation use [ngraph.louvain](https://github.com/anvaka/ngraph.louvain) (it is fast too).

# usage

Install the module:
```
npm i ngraph.louvain.native
```

And then use it:

``` js
let detectClusters = require('ngraph.louvain.native');

let graph = require('miserables'); // ngraph instance

// this would detect clusters
let clusters = detectClusters(graph);

// and you can iterate over them:
graph.forEachNode(function(node) {
  console.log('Node ' + node.id + ' belongs to ' + clusters.getClass(node.id));
});
```

# see also

* https://github.com/anvaka/ngraph.graph - graph structure
* https://github.com/anvaka/ngraph.cw - label-propagation based community detection
* https://github.com/anvaka/ngraph.coarsen - Graph coarser

# license

MIT

# support

If you like what I do, please [support me on patreon](https://www.patreon.com/anvaka).