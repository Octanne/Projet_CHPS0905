# Create a venv if not already created and activate it
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
. .venv/bin/activate
# Install pip and wheel
python -m pip install --upgrade pip
python -m pip install --upgrade wheel


echo "Install LUA if not already  sudo apt install lua5.4"

# SimpleITK installation script with 
# Compilation manuelle de ITK
if [ ! -d "ITK" ]; then
git clone https://github.com/InsightSoftwareConsortium/ITK.git
cd ITK
mkdir ITK-build
cd ITK-build
cmake ../ -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=OFF -DBUILD_TESTING=OFF
make -j8 # Adjust the number of jobs as needed
cd ../..
fi

# Compilation manuelle de Elastix
if [ ! -d "Elastix" ]; then
git clone https://github.com/SuperElastix/elastix.git Elastix
cd Elastix
mkdir build
cd build
ITK_DIR="../../ITK/ITK-build" cmake .. -DCMAKE_BUILD_TYPE=Release -DELASTIX_USE_OPENMP=ON
make -j8 # Adjust the number of jobs as needed
cd ../..
fi

# Compilation manuelle de SimpleITK
if [ ! -d "SimpleITK" ]; then
git clone https://github.com/SimpleITK/SimpleITK.git
cd SimpleITK
mkdir SimpleITK-build
cd SimpleITK-build
ITK_DIR="../../ITK/ITK-build" Elastix_DIR="../../Elastix/build" cmake ../ -DSimpleITK_USE_ELASTIX=ON -DCMAKE_BUILD_TYPE=Release
make -j8 # Adjust the number of jobs as needed
cmake --build . --config Release
cd SimpleITK-build/Wrapping/Python
python setup.py install
cd ../../..
fi