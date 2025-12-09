import { RowsPhotoAlbum } from "react-photo-album";
import "react-photo-album/rows.css";

function cloudDashboard() {
    const photos = [
        { src: "https://art.gametdb.com/wii/cover3D/EN/RMCP01.png?1528403592", width: 800, height: 600 },
        { src: "https://art.gametdb.com/wii/cover3D/US/SMNE01.png?1317736150", width: 800, height: 600 },
    ];

   return <RowsPhotoAlbum photos={photos} />

}

export default cloudDashboard;