import sys

file_path = 'z:/All Data/Documents/Kuliah/smt6/FCT/webgis/sirubi-main/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '''        .garis-utara {
            transform: translate(4px, 4px);
        }
    </style>''',
        '''        .garis-utara {
            transform: translate(4px, 4px);
        }

        .garis-utara-baru {
            transform: translate(6px, 6px);
        }
    </style>'''
    ),
    (
        '''                    <button id="btn-rute-utara" onclick="toggleLayer('ruteUtara', this)"
                        data-route-color="#7f00ff"
                        class="route-btn font-medium py-1 px-4 rounded-sm border-2 flex items-center justify-center gap-2 transition-all">
                        Rute Romokalisari
                    </button>
                    <button id="btn-rute-greges" onclick="toggleLayer('ruteGreges', this)"''',
        '''                    <button id="btn-rute-utara" onclick="toggleLayer('ruteUtara', this)"
                        data-route-color="#7f00ff"
                        class="route-btn font-medium py-1 px-4 rounded-sm border-2 flex items-center justify-center gap-2 transition-all">
                        Rute Romokalisari
                    </button>
                    <button id="btn-rute-utara-baru" onclick="toggleLayer('ruteUtaraBaru', this)"
                        data-route-color="#00bcd4"
                        class="route-btn font-medium py-1 px-4 rounded-sm border-2 flex items-center justify-center gap-2 transition-all">
                        Rute Utara
                    </button>
                    <button id="btn-rute-greges" onclick="toggleLayer('ruteGreges', this)"'''
    ),
    (
        '''            ruteUtara: {
                label: 'Rute Romokalisari',
                type: 'line',
                leafletStyle: { color: '#7f00ff', weight: 4, opacity: 0.9, className: 'garis-utara' },
                legendHtml: `<div style="background-color: #7f00ff; width: 24px; height: 3px;"></div>`
            }
        };''',
        '''            ruteUtara: {
                label: 'Rute Romokalisari',
                type: 'line',
                leafletStyle: { color: '#7f00ff', weight: 4, opacity: 0.9, className: 'garis-utara' },
                legendHtml: `<div style="background-color: #7f00ff; width: 24px; height: 3px;"></div>`
            },
            ruteUtaraBaru: {
                label: 'Rute Utara',
                type: 'line',
                leafletStyle: { color: '#00bcd4', weight: 4, opacity: 0.9, className: 'garis-utara-baru' },
                legendHtml: `<div style="background-color: #00bcd4; width: 24px; height: 3px;"></div>`
            }
        };'''
    ),
    (
        '''            ruteTimur: 'RuteTimur.geojson',
            ruteUtara: 'RuteUtara.geojson'
        };''',
        '''            ruteTimur: 'RuteTimur.geojson',
            ruteUtara: 'RuteUtara.geojson',
            ruteBerangkatUtara: 'Rute_Berangkat_Utara.geojson',
            rutePulangUtara: 'Rute_Pulang_Utara.geojson'
        };'''
    ),
    (
        '''        const layerRuteTimur = L.geoJSON(null, { style: mapStyles.ruteTimur.leafletStyle, onEachFeature: onEachRouteFeature });
        const layerRuteUtara = L.geoJSON(null, { style: mapStyles.ruteUtara.leafletStyle, onEachFeature: onEachRouteFeature });''',
        '''        const layerRuteTimur = L.geoJSON(null, { style: mapStyles.ruteTimur.leafletStyle, onEachFeature: onEachRouteFeature });
        const layerRuteUtara = L.geoJSON(null, { style: mapStyles.ruteUtara.leafletStyle, onEachFeature: onEachRouteFeature });
        const layerRuteUtaraBaru = L.geoJSON(null, { style: mapStyles.ruteUtaraBaru.leafletStyle, onEachFeature: onEachRouteFeature });'''
    ),
    (
        '''        let rawRuteSelatan = null;
        let rawRuteTimur = null;
        let rawRuteUtara = null;''',
        '''        let rawRuteSelatan = null;
        let rawRuteTimur = null;
        let rawRuteUtara = null;
        let rawRuteUtaraBaru = null;'''
    ),
    (
        '''                case 'ruteSelatan': return rawRuteSelatan;
                case 'ruteTimur': return rawRuteTimur;
                case 'ruteUtara': return rawRuteUtara;
                default: return null;''',
        '''                case 'ruteSelatan': return rawRuteSelatan;
                case 'ruteTimur': return rawRuteTimur;
                case 'ruteUtara': return rawRuteUtara;
                case 'ruteUtaraBaru': return rawRuteUtaraBaru;
                default: return null;'''
    ),
    (
        '''            'ruteSelatan': { layer: layerRuteSelatan, active: false },
            'ruteTimur': { layer: layerRuteTimur, active: false },
            'ruteUtara': { layer: layerRuteUtara, active: false }
        };''',
        '''            'ruteSelatan': { layer: layerRuteSelatan, active: false },
            'ruteTimur': { layer: layerRuteTimur, active: false },
            'ruteUtara': { layer: layerRuteUtara, active: false },
            'ruteUtaraBaru': { layer: layerRuteUtaraBaru, active: false }
        };'''
    ),
    (
        '''                try {
                    const resUtara = await fetch(urlGeoJSON.ruteUtara);
                    if (resUtara.ok) rawRuteUtara = await resUtara.json();
                } catch (e) { console.warn('Gagal memuat RuteUtara.json', e); }

                updateSearchData();''',
        '''                try {
                    const resUtara = await fetch(urlGeoJSON.ruteUtara);
                    if (resUtara.ok) rawRuteUtara = await resUtara.json();
                } catch (e) { console.warn('Gagal memuat RuteUtara.json', e); }

                try {
                    const resBU = await fetch(urlGeoJSON.ruteBerangkatUtara);
                    const resPU = await fetch(urlGeoJSON.rutePulangUtara);
                    if (resBU.ok && resPU.ok) {
                        const dataBU = await resBU.json();
                        const dataPU = await resPU.json();
                        
                        dataBU.features.forEach(f => { if(!f.properties) f.properties={}; f.properties.symbolid = "0"; });
                        dataPU.features.forEach(f => { if(!f.properties) f.properties={}; f.properties.symbolid = "1"; });
                        
                        rawRuteUtaraBaru = {
                            type: 'FeatureCollection',
                            features: [...dataBU.features, ...dataPU.features]
                        };
                    }
                } catch (e) { console.warn('Gagal memuat Rute_Berangkat_Utara/Pulang', e); }

                updateSearchData();'''
    ),
    (
        '''                { key: 'ruteTimur', btnId: 'btn-rute-timur' },
                { key: 'ruteBarat', btnId: 'btn-rute-barat' },
                { key: 'ruteUtara', btnId: 'btn-rute-utara' },
                { key: 'ruteGreges', btnId: 'btn-rute-greges' },''',
        '''                { key: 'ruteTimur', btnId: 'btn-rute-timur' },
                { key: 'ruteBarat', btnId: 'btn-rute-barat' },
                { key: 'ruteUtara', btnId: 'btn-rute-utara' },
                { key: 'ruteUtaraBaru', btnId: 'btn-rute-utara-baru' },
                { key: 'ruteGreges', btnId: 'btn-rute-greges' },'''
    ),
    (
        '''                <div class="flex items-center gap-2 text-[#E3242B] text-sm"><div class="w-6 flex justify-center">${mapStyles.ruteTimur.legendHtml}</div><span>${mapStyles.ruteTimur.label}</span></div>
                <div class="flex items-center gap-2 text-[#E3242B] text-sm"><div class="w-6 flex justify-center">${mapStyles.ruteUtara.legendHtml}</div><span>${mapStyles.ruteUtara.label}</span></div>
            `;
        }
        buildLegend();

        function buildBasemapLegend() {
            const container = document.getElementById('map-legend-list');
            if (!container) return;
            const parts = [];
            // Halte & Sekolah
            parts.push(`<div class="legend-item"><div class="legend-swatch" style="background:transparent; display:inline-flex; align-items:center; justify-content:center;">${mapStyles.halte.legendHtml}</div><div>${mapStyles.halte.label}</div></div>`);
            parts.push(`<div class="legend-item"><div class="legend-swatch" style="background:transparent; display:inline-flex; align-items:center; justify-content:center;">${mapStyles.sekolah.legendHtml}</div><div>${mapStyles.sekolah.label}</div></div>`);

            // Rute warna
            const routeKeys = ['ruteExisting', 'ruteBarat', 'ruteGreges', 'ruteSelatan', 'ruteTimur', 'ruteUtara'];''',
        '''                <div class="flex items-center gap-2 text-[#E3242B] text-sm"><div class="w-6 flex justify-center">${mapStyles.ruteTimur.legendHtml}</div><span>${mapStyles.ruteTimur.label}</span></div>
                <div class="flex items-center gap-2 text-[#E3242B] text-sm"><div class="w-6 flex justify-center">${mapStyles.ruteUtara.legendHtml}</div><span>${mapStyles.ruteUtara.label}</span></div>
                <div class="flex items-center gap-2 text-[#E3242B] text-sm"><div class="w-6 flex justify-center">${mapStyles.ruteUtaraBaru.legendHtml}</div><span>${mapStyles.ruteUtaraBaru.label}</span></div>
            `;
        }
        buildLegend();

        function buildBasemapLegend() {
            const container = document.getElementById('map-legend-list');
            if (!container) return;
            const parts = [];
            // Halte & Sekolah
            parts.push(`<div class="legend-item"><div class="legend-swatch" style="background:transparent; display:inline-flex; align-items:center; justify-content:center;">${mapStyles.halte.legendHtml}</div><div>${mapStyles.halte.label}</div></div>`);
            parts.push(`<div class="legend-item"><div class="legend-swatch" style="background:transparent; display:inline-flex; align-items:center; justify-content:center;">${mapStyles.sekolah.legendHtml}</div><div>${mapStyles.sekolah.label}</div></div>`);

            // Rute warna
            const routeKeys = ['ruteExisting', 'ruteBarat', 'ruteGreges', 'ruteSelatan', 'ruteTimur', 'ruteUtara', 'ruteUtaraBaru'];'''
    )
]

new_content = content
for i, (old_text, new_text) in enumerate(replacements):
    if old_text not in new_content:
        print(f'Failed to find replacement {i}')
        sys.exit(1)
    new_content = new_content.replace(old_text, new_text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Success!')
