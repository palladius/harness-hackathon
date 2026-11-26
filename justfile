# Default recipe: list available commands
list:
    @just -l

# Run unit tests and hygiene checks
test:
    python3 -m unittest discover -s tests -v

# Grade a single round directory (e.g. just grade round1-pre-riccardo rag)
grade dir="round1-pre-riccardo" track="arch" scenario="02":
    python3 grader.py {{dir}} --track {{track}} --scenario {{scenario}}

# Compare Pre-Riccardo vs Post-Riccardo side by side
compare r1="round1-pre-riccardo" r2="round2-post-riccardo" track="arch" scenario="02":
    python3 grader.py --compare {{r1}} {{r2}} --track {{track}} --scenario {{scenario}}

# Compile the 6-slide standalone HTML deck with Marp
build-slides:
    marp slides/slides.md --html --allow-local-files -o slides/index.html < /dev/null

# Export PNG previews of all 6 slides for visual QA
preview-slides:
    mkdir -p slides/previews
    marp slides/slides.md --images png --image-scale 1 --html --allow-local-files -o slides/previews/slide.png < /dev/null
