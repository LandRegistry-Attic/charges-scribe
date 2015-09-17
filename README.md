# Scribe

The Scribe app is a part of the Charges "Sign your Mortgage" service. It
provides the document signing functions that the service needs to create a
legally binding digital signature.

Currently for Alpha the Scribe will perform signatures itself. By Live our plan
is for the Scribe to handoff document signing to a Hardware Security Module,
acting as a facade over this hardware.

## Contents
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Changing the migration](#changing-the-migration)
- [Current Model](#current-model)
- [Testing](#testing)

## Usage
GET     /key                                        # get all keys
POST    /deed/<deed_id>/<borrower_id>/signature/    # sign the mortgage deed

## Getting started

Get the git submodules
```
git submodule init
git submodule update
```

Install the requirements
```
pip install -r requirements.txt
pip install -r requirements_test.txt
```

Export your database URI
```
export DATABASE_URI=postgresql://username:password@localhost/database
```

To run the migration run the command
```
python run.py db upgrade head
```

To run the application run the command
```
python run.py runserver

## Changing the migration
All you have to do is change/create the related model and run the command

```
python run.py db revision --autogenerate
```

> For some helpful documentation on using alembic go [here](alembic.md)

## Current model

Key

{
    "id": 24,
    "public_key": "PUBLIC_KEY",
    "private_key": "PRIVATE_KEY"
}

## Testing

### Unit tests

Run the unit tests
```
python tests.py
```

### Acceptance tests

All of the acceptance tests are contained within the acceptance-tests folder with the feature files under the features folder and the step-definitions under the steps folder.

If you would like to run all of the acceptance tests then navigate into the acceptance-tests folder and run the following command:

```
./run_tests.sh
```

You can also pass arguments to this command as you would if you were just running cucumber on it's own.

For example you can use the following command to display a cut down version of cucumbers progress when it is running:

```
./run_tests.sh --format progress
```

Or you can use the following to run only the scenarios that have been tagged with whatever tags you specify:

```
/run_tests.sh --tags @USXX
```

### Running Rubocop

Rubocop is ruby gem that will check any ruby code in the repository against the ruby style guide and then provide a report of any offenses.

In order to run Rubocop on the acceptance test code then navigate into the acceptance test folder and run the command:

```
./run_linting.sh
```

If you wish to amend what cops are used, what files are ignored when running Rubocop then you will need to put this in the rubocop.yml file.
