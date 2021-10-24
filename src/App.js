import React, { useRef, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax

mapboxgl.accessToken = 'pk.eyJ1IjoiYWhvYmJ5OTgiLCJhIjoiY2t1OHRoaGtpMDBieDJvcWp0OGZoN2pzbyJ9.7o5aIZFLVU4mnhXKFYMV3g';

export default function App() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng, setLng] = useState(-84.3880);
    const [lat, setLat] = useState(33.7490);
    const [zoom, setZoom] = useState(9);

    // Set marker options.
    const marker = new mapboxgl.Marker({
    color: "#FFFFFF",
    draggable: false
    }).setLngLat([-84.3880, 33.7490])
    .addTo(map);

    useEffect(() => {
        if (map.current) return; // initialize map only once
            map.current = new mapboxgl.Map({
            container: mapContainer.current,
            style: 'mapbox://styles/mapbox/navigation-day-v1',
            center: [lng, lat],
            zoom: zoom
        });
    });

    useEffect(() => {
        if (!map.current) return; // wait for map to initialize
            map.current.on('move', () => {
            setLng(map.current.getCenter().lng.toFixed(4));
            setLat(map.current.getCenter().lat.toFixed(4));
            setZoom(map.current.getZoom().toFixed(2));
    });
});

return (
    <div>
        <div className="sidebar">
            Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
        </div>
        <div ref={mapContainer} className="map-container" />
    </div>
    );
}