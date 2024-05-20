import { Module } from '@nestjs/common';
import { NamesModule } from './modules/names/names.module';
import { NamesService } from './modules/names/names.service';

@Module({
  imports: [
    NamesModule
  ],
  controllers: [],
  providers: [NamesService],
})
export class AppModule {}
