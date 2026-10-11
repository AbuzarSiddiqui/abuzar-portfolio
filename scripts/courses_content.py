# Course content. Each lesson body is HTML. Quiz "a" is the index of the correct option.
# Edit here, then run: python scripts/build_courses.py

FOUNDATIONS = dict(
slug='foundations-of-ai', title='Foundations of AI',
subtitle='What AI, machine learning and large language models really are — and the difference between generative AI and agentic AI.',
level='Beginner', hours='2 hours', glyph='AI', hue='#2f45e8',
skills=['AI fundamentals', 'Large language models', 'Generative AI', 'Agentic AI', 'Responsible AI'],
outcomes=[
 'Explain AI, machine learning, deep learning and LLMs in plain language',
 'Describe how a language model turns a prompt into an answer',
 'Tell generative AI and agentic AI apart, and know when each fits',
 'Spot the common failure modes of AI systems and design around them',
],
modules=[
 dict(title='What AI actually is', lessons=[
  dict(title='AI, machine learning and deep learning', minutes=10, body='''
<p>“AI” is used for everything from spam filters to self-driving cars, so it helps to start with a simple picture: three nested circles.</p>
<ul>
<li><strong>Artificial intelligence (AI)</strong> is the outer circle — any technique that lets a computer do something we would normally call intelligent: recognising speech, recommending a film, answering a question.</li>
<li><strong>Machine learning (ML)</strong> sits inside it. Instead of a programmer writing every rule, the system <em>learns patterns from examples</em>. Show it thousands of labelled emails and it learns what spam looks like.</li>
<li><strong>Deep learning</strong> is a kind of machine learning that uses large neural networks with many layers. It is what made modern image recognition, speech recognition and language models possible.</li>
</ul>
<h3>Rules versus learning</h3>
<p>Traditional software follows rules: <em>if the order total is over ₹5,000, apply free shipping</em>. Machine learning flips this around. You provide inputs and the desired outputs, and the model works out the pattern. That is powerful when the rules are too complex to write down — like describing what makes a photo “a cat”.</p>
<p>The trade-off is that learned behaviour is <strong>probabilistic</strong>. A rule always gives the same answer; a model gives its best guess, which is usually right and occasionally wrong. That single fact shapes almost every product decision you will make with AI.</p>
''', takeaways=['AI ⊃ machine learning ⊃ deep learning.', 'ML learns patterns from examples instead of hand-written rules.', 'Learned behaviour is probabilistic — design for the occasional wrong answer.']),
  dict(title='How large language models work', minutes=14, body='''
<p>A <strong>large language model (LLM)</strong> — Claude, Gemini, GPT, Llama — is a deep learning model trained on huge amounts of text to do one deceptively simple thing: <em>predict the next piece of text</em>.</p>
<h3>Tokens</h3>
<p>Models don’t read words; they read <strong>tokens</strong> — chunks of text that are often a word, part of a word or a punctuation mark. “Unbelievable” might be split into “un”, “believ”, “able”. Tokens matter because they are how models are <em>measured and priced</em>: context limits and API bills are counted in tokens.</p>
<h3>Training versus inference</h3>
<ul>
<li><strong>Training</strong> is the expensive, one-time phase where the model learns from data. Most models are then refined with human feedback so they follow instructions and behave helpfully.</li>
<li><strong>Inference</strong> is what happens every time you send a prompt: the model reads your tokens and generates new ones, one at a time, each chosen based on everything before it.</li>
</ul>
<h3>The context window</h3>
<p>The <strong>context window</strong> is how much text the model can consider at once — your instructions, any documents you attach, the conversation so far and its own reply. Modern frontier models handle hundreds of thousands to around a million tokens. Anything outside the window, the model simply cannot see.</p>
<blockquote>An LLM doesn’t look facts up. It generates the most plausible continuation of the text in front of it — which is why giving it the right context matters so much.</blockquote>
''', takeaways=['LLMs generate text one token at a time.', 'Tokens are the unit of limits and pricing.', 'The model only knows what is in its training and its context window.']),
 ]),
 dict(title='Generative AI vs agentic AI', lessons=[
  dict(title='Generative AI: creating from a prompt', minutes=10, body='''
<p><strong>Generative AI</strong> is AI that <em>creates new content</em> — text, images, code, audio, video — in response to a prompt. You ask, it produces, you decide what to do with the result.</p>
<h3>What it is good at</h3>
<ul>
<li>Drafting: emails, user stories, release notes, first versions of a spec.</li>
<li>Transforming: summarising a transcript, translating, rewriting for a different audience.</li>
<li>Extracting and classifying: pulling fields out of an invoice, tagging feedback by theme.</li>
<li>Explaining: walking through a concept or a piece of code.</li>
</ul>
<h3>The shape of the interaction</h3>
<p>Generative AI is essentially <strong>one request, one response</strong>. The human stays in control of every step: you read the output, judge it and act on it. That makes it low-risk and easy to adopt — the worst case is a draft you throw away.</p>
<p>Its limit is the same thing: it doesn’t <em>do</em> anything. It can write the Jira ticket, but you still have to create it. It can suggest a SQL query, but it can’t run it and check the result.</p>
''', takeaways=['Generative AI produces content in response to a prompt.', 'One request, one response — the human acts on the output.', 'Low risk, but it can’t take actions on its own.']),
  dict(title='Agentic AI: models that plan and act', minutes=14, body='''
<p><strong>Agentic AI</strong> gives a model the ability to <em>take actions</em> towards a goal. Instead of answering once, an agent works in a loop:</p>
<ol>
<li><strong>Plan</strong> — decide what to do next.</li>
<li><strong>Act</strong> — call a <em>tool</em>: search the web, query a database, read a file, run code, create a ticket.</li>
<li><strong>Observe</strong> — read the result of that action.</li>
<li><strong>Repeat</strong> until the goal is met, then report back.</li>
</ol>
<p>The model is the same kind of LLM as in generative AI. What changes is the <strong>harness</strong> around it: a set of tools it is allowed to use and a loop that feeds results back in.</p>
<h3>A concrete example</h3>
<p>Ask a generative assistant “Is Sprint 24 on track?” and it can only answer from what you paste in. Ask an agent connected to Jira and your QA sheet, and it can fetch the sprint, read the open tickets, check failed tests, and come back with a sourced answer: “Three stories have no acceptance criteria; PAY-112 is blocked by a failed test.”</p>
<h3>The autonomy spectrum</h3>
<p>Agents range from <em>suggest-only</em> (drafts actions for a human to approve) to <em>fully autonomous</em> (acts without asking). In business settings the sweet spot is usually in between: let the agent read and draft freely, and require human approval for anything irreversible — sending a message, changing a record, spending money.</p>
''', takeaways=['Agents loop: plan → act with tools → observe → repeat.', 'Same model; the difference is tools plus a loop.', 'Keep humans approving irreversible actions.']),
  dict(title='Choosing between generative and agentic', minutes=10, body='''
<p>Agents are exciting, but they cost more, take longer and can fail in more ways than a single prompt. Start with the simplest thing that works and only move up when you need to.</p>
<h3>Three levels to choose from</h3>
<ul>
<li><strong>Single call</strong> — classification, summarisation, extraction, Q&amp;A over provided text.</li>
<li><strong>Workflow</strong> — a fixed sequence you design in code (extract → check → draft), with the model doing one step at a time.</li>
<li><strong>Agent</strong> — open-ended tasks where the steps can’t be known in advance.</li>
</ul>
<h3>Four questions before you build an agent</h3>
<ol>
<li><strong>Complexity:</strong> is the task multi-step and hard to fully specify up front?</li>
<li><strong>Value:</strong> does the outcome justify the extra cost and latency?</li>
<li><strong>Viability:</strong> is the model actually capable at this kind of task?</li>
<li><strong>Cost of error:</strong> can mistakes be caught and recovered from — through review, tests or rollback?</li>
</ol>
<p>If the answer to any of these is “no”, stay at a simpler level. A well-designed workflow beats an unreliable agent every time.</p>
''', takeaways=['Prefer single call → workflow → agent, in that order.', 'Use the four questions: complexity, value, viability, cost of error.', 'A reliable workflow beats an unreliable agent.']),
 ]),
 dict(title='Using AI responsibly', lessons=[
  dict(title='Limits, risks and human oversight', minutes=12, body='''
<p>Every AI system you ship will sometimes be wrong. Responsible AI is mostly about designing for that reality.</p>
<h3>The common failure modes</h3>
<ul>
<li><strong>Hallucination</strong> — confident, plausible, wrong output. Reduce it by grounding the model in real data and asking it to cite sources.</li>
<li><strong>Bias</strong> — models learn patterns from human data, including unfair ones. Test outputs across different user groups.</li>
<li><strong>Privacy and data handling</strong> — know what data you send to a model provider, how long it is retained and whether it is used for training.</li>
<li><strong>Over-trust</strong> — users stop checking once outputs look good. Make evidence visible so checking is easy.</li>
</ul>
<h3>Design patterns that help</h3>
<ul>
<li><strong>Cite the source</strong> behind every claim, so a human can verify it in one click.</li>
<li><strong>Say “I don’t know”</strong> when the data doesn’t cover the question, instead of guessing.</li>
<li><strong>Ask when uncertain</strong> — “Does this test belong to PAY-112 or PAY-118?” costs seconds; a wrong guess can cost a release.</li>
<li><strong>Human approval for irreversible actions.</strong></li>
</ul>
<p>These aren’t limitations bolted on at the end. They are what make people willing to rely on the system at all.</p>
''', takeaways=['Expect hallucination, bias, privacy and over-trust risks.', 'Ground, cite, admit uncertainty, ask when unsure.', 'Human approval on irreversible actions builds trust.']),
 ]),
],
quiz=[
 dict(q='Which statement best describes machine learning?', o=['Software that follows rules a programmer writes by hand', 'Systems that learn patterns from examples instead of explicit rules', 'Any software that uses a database', 'A type of computer hardware'], a=1),
 dict(q='What is a token?', o=['A password for an API', 'A chunk of text — often a word or part of a word — that models read and are priced by', 'A unit of GPU memory', 'A single sentence'], a=1),
 dict(q='What does the context window limit?', o=['How many users can call the model at once', 'How much text the model can consider in one request, including its reply', 'How long the model was trained for', 'How many languages it speaks'], a=1),
 dict(q='What is the key difference between generative and agentic AI?', o=['Agentic AI uses a completely different kind of model', 'Agentic AI can only make images', 'Agentic AI uses tools in a loop to take actions towards a goal', 'Generative AI is always more expensive'], a=2),
 dict(q='Which is the right order to consider, from simplest to most complex?', o=['Agent → workflow → single call', 'Single call → workflow → agent', 'Workflow → agent → single call', 'Always start with an agent'], a=1),
 dict(q='An agent can create, edit and close Jira tickets. What is the safest design?', o=['Let it act freely so it is fast', 'Let it read and draft freely; require human approval for changes', 'Never connect it to Jira', 'Only let it run at night'], a=1),
 dict(q='Which practice most directly reduces the impact of hallucination?', o=['Making responses longer', 'Grounding answers in real data and citing the source of each claim', 'Using more emojis', 'Hiding uncertainty from users'], a=1),
 dict(q='The “cost of error” question asks…', o=['How much the API costs per token', 'Whether mistakes can be caught and recovered from', 'How many errors the code has', 'Whether the team has budget'], a=1),
],
)

CLAUDE_CODE = dict(
slug='claude-code-for-professionals', title='Claude Code: How AI Agents Change Your Work',
subtitle='What Claude Code is, what it means for product managers, engineers and designers, and how to work with it safely and well.',
level='Beginner', hours='2 hours', glyph='&gt;_', hue='#c96442',
skills=['Claude Code', 'Agentic coding', 'Prompting for agents', 'AI-assisted prototyping', 'Guardrails'],
outcomes=[
 'Explain what Claude Code is and where it runs',
 'Identify concrete ways it changes your role — PM, engineer or designer',
 'Set up a project so the agent follows your team’s rules',
 'Use permissions, reviews and approvals to keep work safe',
],
modules=[
 dict(title='Meet Claude Code', lessons=[
  dict(title='What Claude Code is', minutes=10, body='''
<p><strong>Claude Code</strong> is Anthropic’s agentic coding tool. Instead of chatting about code in a browser tab, it works <em>inside your project</em>: it can read your files, search the codebase, edit code, run commands and tests, and explain what it did.</p>
<h3>Where it runs</h3>
<p>Claude Code is available in the terminal (as a command-line tool), as a desktop app, on the web, and inside IDEs such as VS Code and JetBrains. The surface changes; the idea is the same — an agent that operates on a real project with your permission.</p>
<h3>How it differs from a chatbot</h3>
<ul>
<li><strong>It has context.</strong> It reads the actual code instead of the snippet you remembered to paste.</li>
<li><strong>It takes actions.</strong> It edits files and runs commands, then checks the result.</li>
<li><strong>It asks permission.</strong> Actions go through a permission system you control, from “ask me every time” to pre-approved commands.</li>
</ul>
<p>In the language of the Foundations course, Claude Code is an <em>agent</em>: a model with tools (file editing, shell, search) running in a loop.</p>
''', takeaways=['Claude Code is an agent that works inside your project.', 'Runs in terminal, desktop, web and IDEs.', 'It reads, edits, runs and verifies — with your permission.']),
  dict(title='How a session actually works', minutes=10, body='''
<p>A typical Claude Code session looks like a conversation with a very fast colleague who can touch the keyboard:</p>
<ol>
<li><strong>You describe the goal</strong> in plain language: “Add a full-screen button to the launch video.”</li>
<li><strong>It explores</strong>: finds the relevant files, reads how the video player works today.</li>
<li><strong>It plans and edits</strong>: makes the change across the files that need it.</li>
<li><strong>It verifies</strong>: runs the app or tests, checks for errors, looks at the result.</li>
<li><strong>It reports</strong>: what changed, what it checked, and anything it couldn’t verify.</li>
</ol>
<p>You stay in the loop the whole time — approving commands, redirecting it (“smaller photo, please”), and deciding what gets committed and shipped.</p>
<h3>A real example</h3>
<p>This portfolio — the redesign, the launch film section, the articles and these courses — was built in conversation with Claude Code. The pattern was always the same: describe the outcome, let the agent do the legwork, review the result, and approve anything that goes live.</p>
''', takeaways=['Goal → explore → edit → verify → report.', 'You approve actions and steer direction.', 'Shipping decisions stay with the human.']),
 ]),
 dict(title='How it changes your role', lessons=[
  dict(title='For product managers', minutes=12, body='''
<p>Claude Code is not only for engineers. For product managers it collapses the distance between an idea and something people can click on.</p>
<ul>
<li><strong>Prototypes in hours, not sprints.</strong> A clickable prototype makes a discussion concrete faster than any slide.</li>
<li><strong>Answers from the code itself.</strong> “How does our discount logic actually work?” — ask the agent to read the codebase and explain it, with file references.</li>
<li><strong>Data without waiting.</strong> Draft and run the query or script that answers a product question, instead of filing a request.</li>
<li><strong>Better specs.</strong> Ground PRDs and acceptance criteria in how the system really behaves today.</li>
<li><strong>Internal tools.</strong> Small dashboards and automations that would never make the engineering roadmap.</li>
</ul>
<h3>What doesn’t change</h3>
<p>Judgment. Deciding <em>what</em> to build, for whom, and why — and saying no to the rest — is still the job. The agent makes building cheaper, which makes choosing well <em>more</em> important, not less.</p>
''', takeaways=['PMs can prototype, investigate and analyse directly.', 'Ground specs in how the system actually works.', 'Cheaper building makes prioritisation more important.']),
  dict(title='For engineers and designers', minutes=10, body='''
<h3>Engineers</h3>
<ul>
<li>Delegate the well-specified work — migrations, test coverage, repetitive refactors, boilerplate — and spend more time on architecture and review.</li>
<li>Onboard to unfamiliar code faster by asking the agent to trace a flow end to end.</li>
<li>Shift from writing every line to <em>specifying, reviewing and verifying</em>. Code review becomes a core skill, not a chore.</li>
</ul>
<h3>Designers</h3>
<ul>
<li>Turn a design into working front-end code and iterate on the real thing, in the browser, at real screen sizes.</li>
<li>Explore variations quickly — layouts, states, dark mode — and judge them live rather than in static mocks.</li>
</ul>
<h3>For everyone: the new core skill</h3>
<p>The common thread is <strong>clear specification</strong>. The better you can describe the outcome, the constraints and how to check the result, the better the agent performs. Writing a good brief is now a technical skill.</p>
''', takeaways=['Engineers shift towards specifying, reviewing and verifying.', 'Designers iterate on real, working interfaces.', 'Clear specification is the core skill for everyone.']),
 ]),
 dict(title='Working well and safely', lessons=[
  dict(title='Set your project up for success', minutes=12, body='''
<h3>Project instructions (CLAUDE.md)</h3>
<p>A <code>CLAUDE.md</code> file in your project gives Claude Code standing instructions every session: how to run the app, coding conventions, what not to touch, and team rules. For example, the AI PM Agent’s instructions say: draft Jira changes but never create them without approval, check for duplicate stories first, and cite a source for every claim.</p>
<h3>Habits that make sessions go well</h3>
<ul>
<li><strong>State the outcome and how to check it.</strong> “Users can watch the film full screen; verify in the browser.”</li>
<li><strong>Plan before big changes.</strong> Ask for a plan, review it, then let it build.</li>
<li><strong>Keep changes small and reviewable.</strong> One feature per change makes review and rollback easy.</li>
<li><strong>Give feedback like you would to a colleague.</strong> Screenshots and specific corrections work well.</li>
</ul>
<h3>Extending it</h3>
<p>Teams can add <em>skills</em> (packaged instructions for recurring tasks), <em>hooks</em> (automatic checks that run at set moments) and <em>MCP servers</em> (connections to tools like Jira, Confluence or databases). Start without them; add them when a need repeats.</p>
''', takeaways=['CLAUDE.md holds standing project rules.', 'State outcome + how to verify; plan before big changes.', 'Add skills, hooks and MCP when needs repeat.']),
  dict(title='Guardrails: permissions, review and approval', minutes=10, body='''
<p>An agent that can edit files and run commands needs guardrails. Claude Code gives you several layers:</p>
<ul>
<li><strong>Permissions.</strong> Decide which actions need approval each time and which are pre-approved. Start strict; loosen as trust grows.</li>
<li><strong>Review the diff.</strong> Read what changed before you commit. Treat agent code like any other contribution.</li>
<li><strong>Version control.</strong> Work on a branch and commit often — every change becomes easy to undo.</li>
<li><strong>Human approval for outward-facing actions.</strong> Pushing to production, sending messages, deleting data or changing shared systems should always be a deliberate human decision.</li>
<li><strong>Protect secrets.</strong> Keep API keys and credentials out of prompts and out of the repository.</li>
</ul>
<blockquote>The agent can move fast because you can review and reverse. Keep both of those true and you can safely delegate a lot.</blockquote>
''', takeaways=['Use permissions, diffs and version control as layers of safety.', 'Outward-facing and irreversible actions need human approval.', 'Never put secrets in prompts or repos.']),
 ]),
],
quiz=[
 dict(q='What makes Claude Code an “agent” rather than a chatbot?', o=['It only answers questions', 'It uses tools — reading and editing files, running commands — in a loop', 'It runs only in the browser', 'It never asks permission'], a=1),
 dict(q='Where can you use Claude Code?', o=['Only in the terminal', 'Terminal, desktop app, web and IDEs', 'Only inside Jira', 'Only on mobile'], a=1),
 dict(q='What is CLAUDE.md for?', o=['Storing API keys', 'Standing project instructions the agent follows every session', 'A changelog for releases', 'Billing information'], a=1),
 dict(q='For a PM, which is the best use of Claude Code?', o=['Replacing prioritisation decisions', 'Building a quick prototype to make a product discussion concrete', 'Approving its own production deploys', 'Writing performance reviews'], a=1),
 dict(q='What becomes the core skill when working with coding agents?', o=['Typing speed', 'Clear specification of outcome, constraints and how to verify', 'Memorising syntax', 'Avoiding version control'], a=1),
 dict(q='Which action should always be a deliberate human decision?', o=['Reading a file', 'Searching the codebase', 'Pushing a change to production', 'Explaining a function'], a=2),
 dict(q='Why keep agent changes small?', o=['Small changes cost more tokens', 'They are easier to review and roll back', 'Agents cannot edit big files', 'It hides mistakes'], a=1),
 dict(q='Where should API keys live?', o=['In the prompt', 'Committed in the repository', 'Outside prompts and the repo, in a secure store', 'In CLAUDE.md'], a=2),
],
)

TOKENS = dict(
slug='token-optimization-cost-efficiency', title='Token Optimization & AI Cost Efficiency',
subtitle='How AI pricing works, the free wins that cut costs without hurting quality, and how to measure cost per completed task.',
level='Intermediate', hours='2.5 hours', glyph='₹↓', hue='#1f8a4c',
skills=['Token economics', 'Prompt caching', 'Batch processing', 'Model selection', 'Unit economics'],
outcomes=[
 'Read an AI bill: input, output, cached and batched tokens',
 'Apply the free wins — caching, batching and prompt hygiene — first',
 'Make deliberate trade-offs with effort level and model choice',
 'Measure cost per completed task and set budgets',
],
modules=[
 dict(title='Tokens and pricing', lessons=[
  dict(title='How AI pricing works', minutes=12, body='''
<p>Almost every AI API charges <strong>per token</strong>, priced per million tokens (MTok), with separate rates for:</p>
<ul>
<li><strong>Input tokens</strong> — everything you send: system prompt, instructions, documents, conversation history, tool definitions.</li>
<li><strong>Output tokens</strong> — everything the model writes back, including any reasoning it does. Output is typically <em>several times</em> more expensive than input.</li>
</ul>
<h3>A worked example</h3>
<p>At the time of writing, Anthropic lists Claude Sonnet 5.5 at $2 per MTok input and $10 per MTok output, and Claude Haiku 5.5 at $0.10 / $0.50. A request with 10,000 input tokens and 1,000 output tokens on Sonnet 5.5 costs:</p>
<p><code>10,000 × $2/1M + 1,000 × $10/1M = $0.02 + $0.01 = $0.03</code></p>
<p>Three cents sounds trivial — until a feature makes a million calls a month. Then it is $30,000, and the levers in this course matter.</p>
<h3>Hidden input: the conversation</h3>
<p>In a chat or agent, the <em>whole history</em> is sent again on every turn. Turn 20 of a conversation re-sends turns 1–19. This is why long conversations and agent loops get expensive — and why caching (next module) is so effective.</p>
<p><em>Prices change often — always confirm current rates on the provider’s pricing page before you build a business case.</em></p>
''', takeaways=['You pay per million tokens, input and output separately.', 'Output usually costs several times more than input.', 'Chats and agents re-send history every turn.']),
  dict(title='Counting and estimating tokens', minutes=8, body='''
<h3>Rules of thumb</h3>
<p>For English text, a token is roughly three-quarters of a word, so 1,000 tokens is about 750 words. Code, numbers and non-English languages often use more tokens per word. Rules of thumb are fine for a rough business case, but <strong>never for billing-critical maths</strong>.</p>
<h3>Measure, don’t guess</h3>
<ul>
<li>Providers offer <strong>token-counting endpoints</strong> — for example, Anthropic’s API has a count-tokens endpoint that returns the exact input count for a request before you send it.</li>
<li>Every API response reports <strong>usage</strong>: input tokens, output tokens and, where relevant, cached tokens. Log these per request.</li>
<li>Different models can tokenise the same text differently, so re-measure when you switch models.</li>
</ul>
<h3>Build a token profile</h3>
<p>For each feature, record the typical input size, output size and number of calls per task. That profile tells you where the money goes — and which lever to pull first.</p>
''', takeaways=['~750 words ≈ 1,000 tokens in English, as a rough guide.', 'Use token-counting endpoints and logged usage for real numbers.', 'Profile each feature: input, output, calls per task.']),
 ]),
 dict(title='The free wins', lessons=[
  dict(title='Prompt caching', minutes=14, body='''
<p>Many requests start with the same long prefix: a big system prompt, tool definitions, a reference document, the earlier part of a conversation. <strong>Prompt caching</strong> lets the provider store that prefix so later requests read it at a steep discount instead of paying full price again.</p>
<h3>The economics (Anthropic’s API, at the time of writing)</h3>
<ul>
<li>Writing to the cache costs a little more than normal input — about <strong>1.25×</strong> for the default 5-minute cache.</li>
<li>Reading from the cache costs a fraction — around <strong>0.1×</strong> of the normal input price on most models, and less on some newer ones.</li>
<li>With the 5-minute cache, the second request already breaks even. Every request after that is mostly savings.</li>
</ul>
<h3>How to get cache hits</h3>
<ul>
<li><strong>Stable content first, changing content last.</strong> Caching matches the prefix exactly; one changed character invalidates everything after it.</li>
<li><strong>Watch for silent cache-breakers</strong> — a timestamp in the system prompt, tools listed in a different order, per-request IDs near the top.</li>
<li><strong>Verify with usage data.</strong> If the cached-read count stays at zero across repeated requests, something is breaking the prefix.</li>
</ul>
<p>Google’s Gemini API offers context caching too. The details differ by provider, but the principle is the same: never pay full price twice for the same prefix.</p>
''', takeaways=['Cache the long, stable prefix; read it back at a fraction of the price.', 'Put stable content first and changing content last.', 'Verify cache reads in usage data — zero means a cache-breaker.']),
  dict(title='Batching and prompt hygiene', minutes=12, body='''
<h3>Batch what nobody is waiting for</h3>
<p>Not every request needs an instant answer. Nightly report generation, bulk tagging of feedback, evaluating thousands of test cases — these can wait minutes or hours. Batch APIs process such jobs asynchronously at a discount; Anthropic’s Message Batches API, for example, costs <strong>50% less</strong> than standard requests.</p>
<h3>Input hygiene</h3>
<ul>
<li>Send only the context the task needs — retrieve the three relevant documents, not the whole wiki.</li>
<li>Trim prompts written for older models: long lists of “ALWAYS” and “NEVER” rules are often unnecessary now and can even reduce quality.</li>
<li>Drop tool definitions a route never uses.</li>
</ul>
<h3>Output hygiene</h3>
<ul>
<li>Ask for the format you need — “return JSON with these three fields” instead of a friendly essay.</li>
<li>Use structured outputs where available so you don’t pay for retries on malformed responses.</li>
<li>Set sensible maximum output lengths per route.</li>
</ul>
<h3>Loop hygiene for agents</h3>
<p>Agents can waste tokens by re-reading the same files or making redundant tool calls. Give them clear goals, the right tools, and stopping conditions.</p>
''', takeaways=['Batch non-urgent work for big discounts (50% on Anthropic’s Batches API).', 'Send only the context the task needs.', 'Ask for compact, structured outputs.']),
 ]),
 dict(title='Trade-offs and measurement', lessons=[
  dict(title='Effort, model choice and routing', minutes=12, body='''
<p>After the free wins come the levers that trade some capability for cost. Pull them deliberately, with measurement.</p>
<h3>Effort level</h3>
<p>Modern models let you control how hard they think. On Anthropic’s current models this is the <strong>effort</strong> setting (low, medium, high, xhigh, max). Lower effort means less reasoning and fewer tokens. Chat, classification and high-volume routes often do well at low effort; complex coding and long agentic tasks benefit from higher effort.</p>
<h3>Model choice</h3>
<p>Providers offer tiers — for Claude, Haiku (fastest, cheapest), Sonnet (balanced) and Opus (most capable), with prices differing by an order of magnitude or more. Use the smallest model that meets your quality bar <em>for that route</em>.</p>
<h3>Routing — and its hidden cost</h3>
<p>You can send easy requests to a cheap model and hard ones to a strong model. But first test the simpler alternative: the strong model at lower effort. Newer models at low effort often match older models at high effort, and one model means one cache — caches don’t carry across models.</p>
<blockquote>Judge cost per <em>completed task</em>, not per request. A cheap request that needs three retries isn’t cheap.</blockquote>
''', takeaways=['Effort and model tier are the main quality-for-cost levers.', 'Try the strong model at low effort before building a cascade.', 'Optimise cost per completed task, not per request.']),
  dict(title='Measuring cost and setting budgets', minutes=10, body='''
<h3>The metric that matters: cost per completed task</h3>
<p>Divide total AI spend for a feature by the number of tasks it <em>successfully</em> completed — tickets drafted and accepted, questions answered correctly, documents processed. This captures retries, failures and wasted calls that per-request averages hide.</p>
<h3>What to log</h3>
<ul>
<li>Per request: model, input tokens, output tokens, cached tokens, latency, feature/route.</li>
<li>Per task: number of calls, total tokens, outcome (success, failure, human-corrected).</li>
</ul>
<h3>Unit economics</h3>
<p>Compare cost per task with the value of the task: the minutes saved, the revenue enabled, the support ticket avoided. If an AI feature costs ₹4 per task and saves ten minutes of a ₹1,000-per-hour analyst, the case is easy. If it costs more than the value it creates, optimise or rethink.</p>
<h3>Budgets and guardrails</h3>
<ul>
<li>Set spend alerts and per-feature budgets.</li>
<li>Cap agent loops with step or token budgets so a runaway task can’t burn money.</li>
<li>Re-run your measurements after every prompt or model change — costs drift.</li>
</ul>
''', takeaways=['Track cost per completed task, per feature.', 'Compare it with the value each task creates.', 'Use alerts, budgets and loop caps; re-measure after changes.']),
 ]),
],
quiz=[
 dict(q='Which is usually more expensive per token?', o=['Input tokens', 'Output tokens', 'They are always equal', 'Cached tokens'], a=1),
 dict(q='At $2/MTok input and $10/MTok output, what do 10,000 input + 1,000 output tokens cost?', o=['$0.003', '$0.03', '$0.30', '$3.00'], a=1),
 dict(q='Why do long chats and agent loops get expensive?', o=['Models charge per minute', 'The whole history is re-sent as input on every turn', 'Output tokens are free', 'Caching is impossible for chats'], a=1),
 dict(q='What is the best way to get prompt cache hits?', o=['Put a timestamp at the top of the system prompt', 'Put stable content first and changing content last', 'Shuffle tool order each request', 'Use a different model each turn'], a=1),
 dict(q='Which workload suits a batch API?', o=['A live customer chat', 'Nightly tagging of thousands of feedback items', 'Autocomplete while typing', 'A voice assistant'], a=1),
 dict(q='Before building a cheap-model/strong-model cascade, what should you test first?', o=['Removing all prompts', 'The strong model at a lower effort level', 'A third provider', 'Doubling max output tokens'], a=1),
 dict(q='Which metric best reflects real AI cost?', o=['Cost per request', 'Cost per completed task', 'Tokens per second', 'Number of models used'], a=1),
 dict(q='A cache-read count of zero across repeated identical-prefix requests suggests…', o=['Caching is working perfectly', 'Something is breaking the prefix', 'The model is free', 'Output is too long'], a=1),
],
)

AIPM = dict(
slug='ai-product-management', title='AI Product Management',
subtitle='How to discover, specify, ship and measure AI products — from choosing the right problem to evals, trust and cost.',
level='Intermediate', hours='3 hours', glyph='PM', hue='#7a3fe0',
skills=['AI product strategy', 'Evals', 'AI UX & trust', 'Human-in-the-loop design', 'AI metrics'],
outcomes=[
 'Explain what makes AI products different to manage',
 'Choose problems where AI genuinely fits',
 'Write evals and acceptance criteria for probabilistic behaviour',
 'Design for trust, roll out safely and measure what matters',
],
modules=[
 dict(title='What’s different about AI products', lessons=[
  dict(title='Probabilistic products', minutes=12, body='''
<p>Traditional software is <strong>deterministic</strong>: the same input gives the same output, and a bug is a bug. AI products are <strong>probabilistic</strong>: the same input can produce different outputs, and “mostly right” is the normal state.</p>
<h3>What that changes for a PM</h3>
<ul>
<li><strong>Quality is a distribution, not a checkbox.</strong> You don’t ask “does it work?” but “how often is it good enough, and how bad are the failures?”</li>
<li><strong>Specs need examples.</strong> “Summarise the ticket well” is not testable. Twenty example tickets with what a good summary looks like is.</li>
<li><strong>Failure design is product design.</strong> What the user sees when the AI is wrong or unsure matters as much as the happy path.</li>
<li><strong>Costs scale with usage.</strong> Every call has a marginal cost, so unit economics are part of the product spec.</li>
<li><strong>The ground keeps moving.</strong> New models arrive every few months; a feature that was impossible last quarter may be easy now.</li>
</ul>
''', takeaways=['AI quality is a distribution — manage how often and how badly it fails.', 'Specs need concrete examples.', 'Failure UX and unit economics are part of the product.']),
 ]),
 dict(title='Discovery: choosing the right problems', lessons=[
  dict(title='Where AI fits — and where it doesn’t', minutes=14, body='''
<p>The most common AI product mistake is starting from the technology: “we should add AI”. Start, as always, from the problem.</p>
<h3>Good signs a problem suits AI</h3>
<ul>
<li>The work involves <strong>language, images or messy unstructured data</strong> — reading, summarising, classifying, drafting.</li>
<li>A <strong>“mostly right, quickly”</strong> answer beats a perfect answer slowly, and a human can review cheaply.</li>
<li>The task is <strong>frequent and repetitive</strong> enough that small savings compound.</li>
<li>Information is <strong>scattered across tools</strong> and someone spends hours stitching it together.</li>
</ul>
<h3>Warning signs</h3>
<ul>
<li>Errors are costly and hard to detect.</li>
<li>A simple rule or a better form would solve it.</li>
<li>There is no data to ground the model in.</li>
</ul>
<h3>Example: the AI PM Agent</h3>
<p>Product managers spend hours stitching together Jira, QA spreadsheets and meeting notes before every sprint review. The information already exists; the problem is attention. That made it a strong AI fit: unstructured inputs, frequent work, cheap human review — and a clear rule that the agent drafts but never changes Jira without approval.</p>
''', takeaways=['Start from the problem, not the technology.', 'Good fits: unstructured data, frequent tasks, cheap review.', 'If a rule or a form solves it, don’t use AI.']),
 ]),
 dict(title='Specs, evals and trust', lessons=[
  dict(title='Evals are the new spec', minutes=14, body='''
<p>An <strong>eval</strong> is a set of example inputs with a way to judge the outputs. For AI features, evals are the closest thing to a spec — and the main tool for knowing whether a change made things better or worse.</p>
<h3>Building a first eval</h3>
<ol>
<li><strong>Collect 20–50 real examples</strong> covering common cases, edge cases and known failures.</li>
<li><strong>Define “good”</strong> for each — an expected answer, a checklist, or a rubric.</li>
<li><strong>Choose a grading method</strong>: exact match for structured outputs, code checks for formats, human review or a model-as-judge with a clear rubric for open-ended text.</li>
<li><strong>Run it on every change</strong> — new prompt, new model, new tool — and track the score over time.</li>
</ol>
<h3>Acceptance criteria for AI behaviour</h3>
<p>Write criteria that can be checked against the eval, for example:</p>
<ul>
<li>Given a sprint with stories missing acceptance criteria, when the PM asks for a health check, then every flagged story is listed with its ticket ID.</li>
<li>Given a question the connected data can’t answer, then the assistant says so instead of guessing.</li>
</ul>
''', takeaways=['Evals = examples + a way to judge outputs.', 'Start with 20–50 real examples and run them on every change.', 'Write acceptance criteria you can test against the eval.']),
  dict(title='Designing for trust', minutes=12, body='''
<p>Users adopt AI features they can trust and abandon the ones that burn them once. Trust is designed, not hoped for.</p>
<h3>Patterns that build trust</h3>
<ul>
<li><strong>Show the evidence.</strong> Cite the ticket, row or document behind every claim, one click away.</li>
<li><strong>Admit uncertainty.</strong> “I’m not sure whether this belongs to PAY-112 or PAY-118” beats a confident wrong answer.</li>
<li><strong>Drafts before actions.</strong> Let AI prepare; let humans approve anything irreversible.</li>
<li><strong>Easy correction.</strong> Make it effortless to edit, reject or undo — and learn from those signals.</li>
<li><strong>Set expectations.</strong> Tell users what the feature is good at and where to double-check.</li>
</ul>
<h3>Avoid</h3>
<ul>
<li>Over-claiming in marketing — the first visible mistake costs more trust than it would have otherwise.</li>
<li>Hiding the AI — users should know when content is generated.</li>
</ul>
''', takeaways=['Cite evidence and admit uncertainty.', 'Drafts before actions; humans approve the irreversible.', 'Make correction effortless and learn from it.']),
 ]),
 dict(title='Shipping and measuring', lessons=[
  dict(title='Rollout, metrics and iteration', minutes=14, body='''
<h3>Roll out in stages</h3>
<ol>
<li><strong>Internal dogfooding</strong> — the team uses it daily and logs failures.</li>
<li><strong>Limited beta</strong> with friendly users and close feedback.</li>
<li><strong>Gradual rollout</strong> with monitoring, a kill switch and a fallback to the non-AI path.</li>
</ol>
<h3>Measure four things</h3>
<ul>
<li><strong>Quality</strong> — eval scores, plus real-world task success: was the draft accepted? Was the answer correct?</li>
<li><strong>Adoption and retention</strong> — do people come back to the feature after the novelty wears off?</li>
<li><strong>Trust signals</strong> — edit rates, rejection rates, “report a problem” clicks.</li>
<li><strong>Cost per completed task</strong> — against the value each task creates.</li>
</ul>
<h3>Close the loop</h3>
<p>Every rejected draft and corrected answer is a free eval case. Feed real failures back into your eval set, fix, re-run and ship again. And re-test when new models launch — the best improvement to your product might be one model upgrade away.</p>
''', takeaways=['Dogfood → beta → gradual rollout with a kill switch.', 'Measure quality, adoption, trust and cost per task.', 'Turn real failures into eval cases; re-test on new models.']),
 ]),
],
quiz=[
 dict(q='What is the defining difference between AI products and traditional software?', o=['AI products have no UI', 'AI outputs are probabilistic — the same input can give different results', 'AI products never have bugs', 'AI products cannot be measured'], a=1),
 dict(q='Which problem is the strongest fit for AI?', o=['Calculating tax with fixed rules', 'Summarising hundreds of messy customer comments every week', 'Storing passwords', 'A form that needs one extra field'], a=1),
 dict(q='What is an eval?', o=['A performance review', 'A set of example inputs plus a way to judge the outputs', 'A pricing model', 'A marketing claim'], a=1),
 dict(q='How many examples are a sensible start for a first eval?', o=['1', '20–50 real examples', '1 million', 'None — just ship'], a=1),
 dict(q='Which pattern builds user trust?', o=['Hiding that content is AI-generated', 'Citing the source behind each claim', 'Never admitting uncertainty', 'Letting the AI change records without approval'], a=1),
 dict(q='Which rollout plan is safest?', o=['Launch to everyone on day one', 'Dogfood, limited beta, then gradual rollout with a kill switch', 'Skip monitoring to move faster', 'Remove the non-AI fallback'], a=1),
 dict(q='A high draft-rejection rate is mainly a signal about…', o=['Trust and quality', 'Server uptime', 'Brand colours', 'Hiring'], a=0),
 dict(q='What should you do with real-world failures?', o=['Ignore them', 'Add them to the eval set, fix and re-run', 'Delete the logs', 'Switch off the feature permanently'], a=1),
],
)

from course_apis import APIS

COURSES = [FOUNDATIONS, CLAUDE_CODE, APIS, TOKENS, AIPM]
