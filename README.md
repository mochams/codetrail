# 🌲 Codetrail: Where Code Goes Hiking

[![PyPI](https://img.shields.io/pypi/v/codetrail)](https://pypi.org/project/codetrail/)
[![Python](https://img.shields.io/pypi/pyversions/codetrail)](https://pypi.org/project/codetrail/)
![License](https://img.shields.io/github/license/mochams/codetrail)
[![Built with Sheer Determination](https://img.shields.io/badge/Built%20with-Sheer%20Determination-brightgreen.svg)](https://github.com/mochams/codetrail)

## 🤔 What's This All About?

Welcome to the learning experience! First things first: `Codetrail` is not trying to be the next `Git`. Heck, we're actually using `Git` as our version control system. We're just crazy enough to build our own distributed version control system from scratch because... why not?

## 💡 The Mission

We're here to prove that with:

- A dangerous amount of curiosity
- Caffeine (lots of it)
- Sheer, unadulterated determination
- And perhaps a slight dash of madness

You can build a distributed version control system from the ground up. Is it practical? Probably not. Is it educational? Absolutely! Will it be fun? You bet your last semicolon it will be!

## 📑 Design & Documentation

### RFCs (Request for Comments)

We believe in learning by doing, but also in documenting why we did what we did. Each major feature comes with its own RFC in the `/docs/rfcs` directory. These RFCs explain our thinking, design decisions, and implementation details.

Current RFCs:

- [RFC-001: Codetrail Initialize Command](docs/rfcs/CODETRAIL001.md)
- [RFC-010: Codetrail Configuration Command](docs/rfcs/CODETRAIL010.md)
- More to come as we build this thing!

Want to contribute a new feature? Start by reading our existing RFCs to understand our design philosophy, then draft your own RFC before diving into code. We promise to read it, even if it's written on a napkin (digital napkins preferred).

## 🗺️ Roadmap (Or: How We're Building This Thing)

### Phase 1: Baby Steps 🐣

- [x] Project setup (You're looking at it!)
- [x] `init` - Because every journey needs a starting point. ([CODETRAIL001](docs/rfcs/CODETRAIL001.md))
- [x] `config` - Local config only (we're keeping it simple, folks) ([CODETRAIL010](docs/rfcs/CODETRAIL010.md))
- [ ] `add` - Teaching `codetrail` which files to track
- [ ] `commit` - Making our first memories together

### Phase 2: Walking Steadily 🚶

- [ ] `status` - Finding out what's going on
- [ ] `log` - A trip down memory lane
- [ ] `branch` - Because sometimes we need parallel universes
- [ ] `checkout` - Time travel between branches

### Phase 3: Starting to Run 🏃

- [ ] `merge` - Bringing parallel universes together
- [ ] `reset` - For when we mess up (it happens)
- [ ] `revert` - For when we mess up but want to be fancy about fixing it
- [ ] Basic conflict resolution (pray we don't need this)

### Future Dreams 💭

- [ ] Remote repository support
- [ ] Push/pull mechanisms
- [ ] Interactive rebase (because we're ambitious)
- [ ] Whatever cool feature you suggest!

## 🎯 What Makes Codetrail Different?

Unlike other VCS projects that try to compete with Git, we're here to:

- Learn how Git's magic actually works
- Break things (intentionally, of course)
- Fix those things (eventually)
- Document every "aha!" and "oh no!" moment
- Share the journey with fellow code adventurers

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- poetry (Python package manager)

### Basic Usage

```bash
# From PyPI
pip install codetrail

# For development
git clone https://github.com/mochams/codetrail
cd codetrail
poetry install

# Run to see supported commands
codetrail --help

# Run to see usage of a particular command e.g init
codetrail init --help

# Run your command. e.g init
codetrail init
```

## 🤝 Contributing

Found a bug? That's probably a feature! But if you insist, here's how you can help:

### Before You Start

1. Check out our RFCs in `/docs/rfcs` to understand our design decisions
2. Browse through existing issues and pull requests
3. For new features, consider writing an RFC first

### Development Process

1. Clone the repo
2. Create your feature branch
3. Write tests (yes, we're that serious)
4. Commit your changes
5. Push to the branch
6. Open a Pull Request

### RFC Process

1. Check existing RFCs to avoid duplication
2. Use the RFC template in `/docs/rfcs/Template.md`
3. Submit RFC as a pull request
4. Engage in discussion with maintainers
5. Once approved, implement away!

## 👀 Watching the Project

Interested in following our journey? Here's how to stay updated:

- ⭐ Star the repository to show your support
- 👀 Watch the repository for all activity
- 🔔 Follow releases for major updates
- 📖 Check our [Wiki](https://github.com/mochams/codetrail/wiki) for learning resources and documentation

## ⚠️ Warning

If you're looking for a production-ready VCS, you might want to stick with Git. If you're looking for an adventure in code that might occasionally explode in your face (in a good way), you're in the right place!

---

Made with ❤️ and excessive amounts of ☕
