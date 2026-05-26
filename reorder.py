import re

with open(r'z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Define the start and end markers for the section we want to reorder
start_marker = "            <!-- PANEL 1: Rute Eksisting -->"
end_marker = "            <!-- PANEL 6: Aksi Bawah (Lokasi & Reset) -->"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers")
    exit(1)

panels_text = text[start_idx:end_idx]

# Split by "            <!-- PANEL "
parts = panels_text.split("            <!-- PANEL ")

# parts[0] will be empty because it starts with the delimiter
panels = {}
for p in parts[1:]:
    full_str = "            <!-- PANEL " + p
    if "1: Rute Eksisting" in p:
        panels['1'] = full_str
    elif "2: Pencarian" in p:
        panels['2'] = full_str
    elif "2.5: Filter Kategori Sekolah" in p:
        panels['2.5'] = full_str
    elif "3: Legenda" in p:
        panels['3'] = full_str
    elif "4: Basemap Toggle" in p:
        panels['4'] = full_str
    elif "5: Rekomendasi Halte" in p:
        panels['5'] = full_str

new_order = ['2', '1', '5', '2.5', '4', '3']
new_panels_text = "".join([panels[k] for k in new_order])

new_text = text[:start_idx] + new_panels_text + text[end_idx:]

with open(r'z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully reordered panels.")
