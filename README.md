# Flask + Svelte

This is a simple repo showing how to connect Flask + Svelte. It boils down to:

- Store your Svelte project in a directory in the root of your Flask project
- Set a Flask `route` directing any paths not otherwise specified to `svelte/public`
- Set the `main.js` of your Svelte project to target `#svelte-app` or similar (rather than `body`).
- Include `<div id='svelte-app'></div>` in the relevant Jinja template.

That's it!

