git clone https://github.com/ThugPigeon653/ecosystem-model.git
copy ecosystem-model/src/main.py frontend/main.py
copy ecosystem-model/src/ecosystem.py ecosystem/ecosystem.py
copy ecosystem-model/src/world_visualizer.py map/map.py
python frontend/transform_main.py
python ecosystem/transform_ecosystem.py
python map/transform_map.py