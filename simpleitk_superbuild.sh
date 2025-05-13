# Create a venv if not already created and activate it
if [[ ! -d ".venv" ]]; then
    python3 -m venv .venv
fi
. .venv/bin/activate
# Install pip and wheel
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install -r RENDU_Projet/requirement.txt

# Compilation manuelle de SimpleITK
if [[ ! -d "SimpleITK" ]]; then
git clone https://github.com/SimpleITK/SimpleITK.git
cd SimpleITK
mkdir SimpleITK-build
cd SimpleITK-build
cmake ../SuperBuild \
    -DSimpleITK_USE_ELASTIX=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DWRAP_TCL=OFF \
    -DWRAP_LUA=OFF \
    -DWRAP_R=OFF \
    -DWRAP_RUBY=OFF \
    -DWRAP_CSHARP=OFF \
    -DWRAP_JAVA=OFF \
    -DWRAP_PYTHON=ON
make -j$(8)
make -C SimpleITK-build dist
#pip install SimpleITK-build/Wrapping/Python
fi