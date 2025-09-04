# db_row_helper

A simple Python library to simplify database row verification and testing.

## 🚀 Installation

Clone and install locally:

```bash
git clone https://github.com/yourusername/db_row_helper.git
cd db_row_helper
pip install -e .

#install directly in another project:
pip install git+https://github.com/maneshkadam67/db_row_helper.git

#usage
from db_row_helper import helper

# Example: verify row count
helper.verify_row_count(connection, expected=2)
