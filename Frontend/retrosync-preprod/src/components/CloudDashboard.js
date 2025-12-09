import { RowsPhotoAlbum } from "react-photo-album";
import "react-photo-album/rows.css";

function cloudDashboard() {
    const photos = [
        { src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg", width: 800, height: 600 },
        { src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg", width: 1600, height: 900 },
    ];

   return <RowsPhotoAlbum photos={photos} />

}

export default cloudDashboard;