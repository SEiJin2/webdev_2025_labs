import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css'],
})
export class AlbumPhotosComponent implements OnInit {
  photos: any[] = [];
  albumId!: number;

  constructor(
    private route: ActivatedRoute,
    private albumsService: AlbumsService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.albumId = +this.route.snapshot.paramMap.get('id')!;
    this.albumsService.getPhotos(this.albumId).subscribe((data) => (this.photos = data));
  }

  goBack(): void {
    this.router.navigate(['/albums', this.albumId]);
  }
}