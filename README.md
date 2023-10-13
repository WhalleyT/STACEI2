# STACEI
## Getting Started

### Prerequisites

STACEI leverages several pre-existing tools for its analyses:

* [CCP4 suite](http://www.ccp4.ac.uk/)

* [Python 2.7](https://www.python.org/download/releases/2.7/)

* [R](https://www.r-project.org/)

* [PyMol](https://www.schrodinger.com/suites/pymol)

* [ANARCI](http://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/ANARCI.php)

If you run the installation script (setup.py) these will be installed for you.

Python and R generally come pre-installed on most Linux and Mac distributions, but if not they can be downloaded from the above links, or in Ubuntu with:
`sudo apt-get install python2.7`
`sudo apt-get install r-base`

## Installation
### Manually installation

CCP4 can be installed by following the instruction guidlines. It must also be added to the path in order for Python to recognise it when making calls to it. This can be done by either running `./start` from within the CCP4 directory, or by running `source /applications/ccp4-x.y.x/bin/ccp4.setup-sh` and adding it to your BASH path.

PyMol can also be downloaded by following the above link. Conda users can install it using `conda install -c schrodinger pymol` and Ubuntu users can download it with `sudo apt-get install pymol`.

ANARCI must be downloaded by following the link manually, or by installing via ```setuptools```.

### Python package installation
To install, simply clone this repository or download it. Cloning it can be done with:

`git clone github.com/whalleyt/STACEI`

then run:
 `python setup.py install`

This will download the Linux binaries for CCP4, install them as part of the tool and then install everything else via ```setuptools```.

### Docker
A Docker build of the tool is also available. To run your data in a Docker image do the following:

```docker pull twhalley93/stacei```
  

## Authors
Manuscript in  progress

## License

This project is licensed under the GNU GPL License - see the [LICENSE](LICENSE) file for details.
