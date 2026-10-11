# AI APIs Compared course. Facts checked against official provider docs on 2026-10-12; prices move — re-check before editing.

APIS = dict(
slug='ai-apis-compared', title='AI APIs Compared: Claude, Gemini, NVIDIA & Open Models',
subtitle='How AI APIs work, what Claude, Gemini and NVIDIA each offer, and how to choose between proprietary APIs and open-weight models.',
level='Intermediate', hours='3 hours', glyph='{ }', hue='#0a66c2',
skills=['API fundamentals', 'Claude API', 'Gemini API', 'NVIDIA NIM', 'Open-weight models', 'Vendor evaluation'],
outcomes=[
 'Explain how an AI API request works — keys, endpoints, tokens, limits',
 'Describe what the Claude, Gemini and NVIDIA APIs each offer',
 'Weigh open-weight models against proprietary APIs',
 'Run a structured vendor evaluation for your own use case',
],
modules=[
 dict(title='API fundamentals', lessons=[
  dict(title='What an API is and how AI APIs work', minutes=12, body='''
<p>An <strong>API (Application Programming Interface)</strong> is a contract that lets one piece of software ask another for something. Your app sends a <em>request</em>; the service sends back a <em>response</em>. AI APIs work the same way: you send a prompt, the provider runs the model on its servers, and you get the generated text back.</p>
<h3>The anatomy of an AI API call</h3>
<ul>
<li><strong>Endpoint</strong> — the URL you send requests to, for example a “messages” or “chat completions” endpoint.</li>
<li><strong>API key</strong> — a secret that identifies your account and is used for billing. Treat it like a password: never put it in front-end code or a public repository.</li>
<li><strong>Request body (JSON)</strong> — which model to use, your instructions and messages, optional tools, and limits such as maximum output length.</li>
<li><strong>Response</strong> — the generated content, why the model stopped, and a <strong>usage</strong> section counting input and output tokens.</li>
</ul>
<h3>SDKs</h3>
<p>Providers publish official <strong>SDKs</strong> — libraries for Python, TypeScript, Java and more — that wrap the raw HTTP calls, handle retries and give you typed objects. Use them instead of hand-writing HTTP requests.</p>
<h3>Rate limits</h3>
<p>Every provider caps how many requests and tokens you can use per minute. Plan for it: retry with back-off on “too many requests” errors, and request higher limits before a big launch.</p>
''', takeaways=['Request → model runs on the provider’s servers → response.', 'Keys are secrets; responses report token usage.', 'Use official SDKs; plan for rate limits.']),
  dict(title='Capabilities to compare across providers', minutes=10, body='''
<p>Most frontier APIs now offer a similar menu. Knowing the vocabulary makes vendor comparisons much easier.</p>
<ul>
<li><strong>Model tiers</strong> — a most-capable model, a balanced model and a fast, cheap model.</li>
<li><strong>Context window</strong> — how much text fits in one request (frontier models: up to around a million tokens).</li>
<li><strong>Multimodal input</strong> — images, PDFs, audio or video alongside text.</li>
<li><strong>Tool use / function calling</strong> — the model can call functions you define; the foundation for agents.</li>
<li><strong>Structured outputs</strong> — responses guaranteed to match a JSON schema.</li>
<li><strong>Caching</strong> — repeated prompt prefixes billed at a discount.</li>
<li><strong>Batch processing</strong> — asynchronous jobs at a lower price.</li>
<li><strong>Grounding / web search</strong> — answers backed by live search results.</li>
<li><strong>Data handling</strong> — retention, training use and regional processing.</li>
</ul>
<p>The headline benchmark matters less than you’d think. For most products the deciding factors are quality <em>on your own examples</em>, cost per completed task, latency, data terms and how well the API fits your stack.</p>
''', takeaways=['Compare tiers, context, multimodality, tools, structured output, caching, batch, grounding and data terms.', 'Test quality on your own examples, not just benchmarks.']),
 ]),
 dict(title='The providers', lessons=[
  dict(title='The Claude API (Anthropic)', minutes=14, body='''
<p>Anthropic’s <strong>Claude API</strong> is built around one main endpoint, the <strong>Messages API</strong>. Tools, structured outputs and documents are all features of that endpoint, with supporting endpoints for batches, files, token counting and listing models.</p>
<h3>Model line-up (October 2026)</h3>
<ul>
<li><strong>Claude Opus 5.5</strong> — the flagship for complex reasoning, coding and agents ($4 / $20 per million input / output tokens).</li>
<li><strong>Claude Sonnet 5.5</strong> — fast and capable for everyday coding, agent and enterprise work ($2 / $10).</li>
<li><strong>Claude Haiku 5.5</strong> — the fastest, cheapest tier for high-volume tasks ($0.10 / $0.50 for prompts up to 100K tokens).</li>
<li><strong>Claude Fable 5.1</strong> — Anthropic’s most capable widely released model, for the hardest long-horizon work ($10 / $50).</li>
</ul>
<p>Current models offer a context window of up to 1 million tokens.</p>
<h3>Notable capabilities</h3>
<ul>
<li><strong>Adaptive thinking and effort</strong> — the model decides how much to reason; you tune depth and spend with an effort setting.</li>
<li><strong>Tool use</strong> — your own tools, plus Anthropic-hosted web search, web fetch and code execution.</li>
<li><strong>Prompt caching</strong> and the <strong>Message Batches API</strong> (50% cheaper) for cost control.</li>
<li><strong>Citations</strong> on documents, and PDF and image input.</li>
<li><strong>Managed Agents</strong> — Anthropic runs the agent loop and a sandboxed workspace for you.</li>
</ul>
<h3>Where to access it</h3>
<p>Directly through Anthropic’s API, or through cloud platforms including Amazon Bedrock, Google Cloud Vertex AI and Microsoft Foundry — useful when your company already buys from one of them.</p>
<p><em>Prices change; check Anthropic’s pricing page before you commit.</em></p>
''', takeaways=['One Messages API with tools, structured output, caching and batches.', 'Tiers: Haiku (cheap) → Sonnet → Opus → Fable (most capable).', 'Available directly or via Bedrock, Vertex AI and Foundry.']),
  dict(title='The Gemini API (Google)', minutes=12, body='''
<p>Google offers Gemini models through two front doors that share the same Google GenAI SDK:</p>
<ul>
<li><strong>Gemini Developer API</strong> via <strong>Google AI Studio</strong> — sign up with an API key; Google recommends it for most developers.</li>
<li><strong>Vertex AI</strong> on Google Cloud — for enterprise controls, Cloud identity and regions, and integration with the rest of Google Cloud.</li>
</ul>
<h3>Model line-up (October 2026)</h3>
<ul>
<li><strong>Gemini 3.1 Pro</strong> (preview) — complex reasoning, agents and coding.</li>
<li><strong>Gemini 3.8 Flash</strong> — Google’s most capable Flash model, recommended for most new projects.</li>
<li><strong>Gemini 3.5 Flash-Lite</strong> — the fastest, cheapest tier for high volume.</li>
</ul>
<p>These models accept text, images, video, audio and PDFs, with a context window of about 1 million input tokens.</p>
<h3>Notable capabilities</h3>
<ul>
<li>Function calling, structured outputs, code execution and context caching.</li>
<li><strong>Grounding with Google Search</strong> and Google Maps — a distinctive strength for questions that need fresh information.</li>
<li>Batch processing at 50% of standard prices.</li>
<li>A <strong>free tier</strong> for Flash and Flash-Lite. Note: on the free tier, content may be used to improve Google’s products; on the paid tier it is not.</li>
</ul>
<h3>Pricing snapshot</h3>
<p>Per million tokens on the paid tier: 3.8 Flash $0.75 input / $3.75 output (Google has announced these double on 1 January 2027); 3.5 Flash-Lite $0.30 / $2.50; 3.1 Pro $2 / $12 for prompts up to 200K tokens.</p>
''', takeaways=['Two routes: AI Studio (simple) or Vertex AI (enterprise).', 'Pro, Flash and Flash-Lite tiers; strong multimodal and Search grounding.', 'A free tier exists — check its data terms.']),
  dict(title='NVIDIA APIs and open models', minutes=14, body='''
<p>NVIDIA plays a different role from Anthropic and Google. Rather than offering only its own models through a hosted API, it provides the <strong>infrastructure to run many models</strong> — including open-weight models you can host yourself.</p>
<h3>NVIDIA NIM</h3>
<p><strong>NIM (NVIDIA Inference Microservices)</strong> packages models as optimised containers that run on NVIDIA GPUs — in any cloud, your own data centre or a workstation. NIM exposes <strong>OpenAI-compatible endpoints</strong>, so apps written for that common format can switch to a NIM-served model with minimal code changes.</p>
<h3>The API catalog (build.nvidia.com)</h3>
<p>NVIDIA hosts a catalog of models you can call over an API for prototyping. It includes NVIDIA’s own models and many third-party open-weight models — Llama, Mistral, DeepSeek, Qwen, Gemma, gpt-oss and others. Joining the free NVIDIA Developer Program gives access to hosted endpoints for prototyping and to self-hosted NIM for research and testing.</p>
<h3>Going to production</h3>
<p>Self-hosting NIM in production requires an <strong>NVIDIA AI Enterprise</strong> licence, priced per GPU (NVIDIA’s FAQ lists from $4,500 per GPU per year, with a 90-day trial). Alternatively, many inference providers serve the same open models and charge per token.</p>
<h3>Nemotron: NVIDIA’s own models</h3>
<p>The <strong>Nemotron</strong> family comes in Nano, Super and Ultra sizes, for everything from lightweight sub-agents to the hardest reasoning. NVIDIA publishes the weights, and its Nemotron Open Model License allows commercial use. Licences can vary by model, so always read the model card.</p>
<h3>Other NVIDIA tools you may hear about</h3>
<ul>
<li><strong>NeMo</strong> — a framework for training and fine-tuning generative models, plus guardrail and retrieval components.</li>
<li><strong>Riva</strong> — GPU-accelerated speech recognition and text-to-speech.</li>
</ul>
''', takeaways=['NVIDIA provides infrastructure to run many models, not one hosted model.', 'NIM: GPU-optimised containers with OpenAI-compatible endpoints.', 'Free to prototype; production self-hosting needs an AI Enterprise licence.']),
 ]),
 dict(title='Choosing the right option', lessons=[
  dict(title='Open-weight models vs proprietary APIs', minutes=12, body='''
<h3>Open-weight is not always open-source</h3>
<p>An <strong>open-weight</strong> model publishes its trained weights so you can download and run it. That is not the same as <strong>open-source</strong> in the strict sense, which also covers licence freedoms and often the training data and code. Many “open” models use custom licences with conditions. Read the licence before you build on one.</p>
<h3>The trade-offs</h3>
<div class="tbl-wrap"><table class="tbl">
<tr><th></th><th>Proprietary API (Claude, Gemini)</th><th>Open-weight, self-hosted (e.g. via NIM)</th></tr>
<tr><td>Setup</td><td>Minutes — get a key and call it</td><td>GPUs, containers, scaling and updates to run</td></tr>
<tr><td>Cost shape</td><td>Pay per token; no fixed cost</td><td>Fixed GPU and licence costs; can be cheaper per call at high, steady volume</td></tr>
<tr><td>Data control</td><td>Governed by the provider’s terms and tier</td><td>Data stays on infrastructure you control</td></tr>
<tr><td>Capabilities</td><td>Frontier models plus hosted extras (search, caching, agents)</td><td>Depends on the model; you build the extras</td></tr>
<tr><td>Customisation</td><td>Prompting; limited fine-tuning</td><td>Full control, including fine-tuning</td></tr>
</table></div>
<p>Many companies use both: a proprietary frontier model for the hardest, highest-value tasks, and an open model for high-volume or data-sensitive workloads.</p>
''', takeaways=['Open-weight ≠ open-source; always read the licence.', 'APIs: fast start, pay-per-use. Self-hosting: control, fixed costs, ops burden.', 'Many teams mix both.']),
  dict(title='A vendor evaluation framework', minutes=12, body='''
<p>Choosing an AI provider is a product decision. Use a simple, repeatable process.</p>
<ol>
<li><strong>Define the job.</strong> Write down the task, inputs, expected outputs and quality bar.</li>
<li><strong>Build a small eval.</strong> 20–50 real examples with a clear definition of a good answer.</li>
<li><strong>Shortlist two or three options</strong> — for example, a Claude tier, a Gemini tier and an open model via NIM.</li>
<li><strong>Run the eval on each.</strong> Score quality, and record latency and token usage.</li>
<li><strong>Calculate cost per completed task</strong> at your expected volume, including caching and batch discounts.</li>
<li><strong>Check the non-functionals:</strong> data retention and training terms, regional processing, compliance, rate limits, SLAs and support.</li>
<li><strong>Consider switching cost.</strong> Keep prompts and evals portable, and isolate provider-specific code behind one module.</li>
</ol>
<blockquote>The “best model” is the one that meets your quality bar on your examples at the lowest cost per completed task, with data terms your company accepts.</blockquote>
<p>Re-run the evaluation every few months. New models launch constantly, and prices move in both directions.</p>
''', takeaways=['Evaluate on your own examples, not leaderboards.', 'Compare cost per completed task and data terms.', 'Keep prompts and evals portable; re-evaluate regularly.']),
 ]),
],
quiz=[
 dict(q='What does an API key do?', o=['Speeds up the model', 'Identifies your account for access and billing — keep it secret', 'Chooses the model automatically', 'Encrypts the response'], a=1),
 dict(q='Which part of an API response tells you what a request cost?', o=['The endpoint URL', 'The usage section with input and output token counts', 'The model name', 'The HTTP method'], a=1),
 dict(q='Which provider is known for grounding answers with Google Search?', o=['Anthropic Claude', 'Google Gemini', 'NVIDIA NIM', 'None of them'], a=1),
 dict(q='What is NVIDIA NIM?', o=['A chatbot app', 'GPU-optimised containers for serving models, with OpenAI-compatible endpoints', 'A web browser', 'A pricing plan for Claude'], a=1),
 dict(q='Which Claude tier is designed for high-volume, low-cost tasks?', o=['Fable', 'Opus', 'Haiku', 'Sonnet'], a=2),
 dict(q='“Open-weight” means…', o=['The model is free for any use, no conditions', 'The trained weights are published so you can run the model — licence terms still apply', 'The model has no licence', 'The model only runs in a browser'], a=1),
 dict(q='When does self-hosting an open model tend to make sense?', o=['At very low, occasional volume', 'At high, steady volume or when data must stay on your infrastructure', 'Never', 'Only for image models'], a=1),
 dict(q='What is the best basis for choosing a provider?', o=['The top public leaderboard score', 'Quality on your own examples and cost per completed task, within acceptable data terms', 'Whichever has the most models', 'The newest logo'], a=1),
],
)
