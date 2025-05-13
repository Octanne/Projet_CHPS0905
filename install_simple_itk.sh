# Create a venv if not already created and activate it
if [[ ! -d ".venv" ]]; then
    python3 -m venv .venv
fi
. .venv/bin/activate
# Install pip and wheel
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install -r RENDU_Projet/requirement.txt

echo "Install LUA if not already ex: sudo apt install lua5.4"

# SimpleITK installation script with 
# Compilation manuelle de ITK
if [[ ! -d "ITK" ]]; then
git clone https://github.com/InsightSoftwareConsortium/ITK.git
cd ITK
mkdir ITK-build
cd ITK-build
cmake ../ -DCMAKE_CXX_STANDARD=17 -DCMAKE_CXX_FLAGS="-include cstdint" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=OFF -DBUILD_TESTING=OFF
make -j8 # Adjust the number of jobs as needed
cd ../..
fi

# Compilation manuelle de Elastix
if [[ ! -d "Elastix" ]]; then
git clone https://github.com/SuperElastix/elastix.git Elastix
cd Elastix
mkdir build
cd build
ITK_DIR="../../ITK/ITK-build" cmake .. -DCMAKE_CXX_STANDARD=17 -DCMAKE_CXX_FLAGS="-include cstdint" -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Release -DELASTIX_USE_OPENMP=ON
make -j8 # Adjust the number of jobs as needed
cd ../..
fi

# Compilation manuelle de SimpleITK
if [[ ! -d "SimpleITK" ]]; then
git clone https://github.com/SimpleITK/SimpleITK.git
cd SimpleITK
mkdir SimpleITK-build
cd SimpleITK-build
ITK_DIR="../../ITK/ITK-build" Elastix_DIR="../../Elastix/build" cmake ../ -DSimpleITK_USE_ELASTIX=ON -DCMAKE_BUILD_TYPE=Release -DWRAP_LUA=OFF -DWRAP_CSHARP=OFF -DWRAP_JAVA=OFF -DWRAP_PYTHON=ON
make -j8 # Adjust the number of jobs as needed
cmake --build . --config Release
cd Wrapping/Python
python setup.py install
cd ../../..
fi