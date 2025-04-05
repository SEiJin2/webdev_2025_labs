import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css'],
})
export class AlbumDetailComponent implements OnInit {
  album: any = {};
  id!: number;

  constructor(
    private route: ActivatedRoute,
    private albumsService: AlbumsService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('id')!;
    this.albumsService.getAlbum(this.id).subscribe((data) => (this.album = data));
  }

  save(): void {
    this.albumsService.updateAlbum(this.id, this.album).subscribe();
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }

  viewPhotos(): void {
    this.router.navigate(['/albums', this.id, 'photos']);
  }
}