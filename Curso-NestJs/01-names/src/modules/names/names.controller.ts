import { Body, Controller, Delete, Get, Post, Query, Param, Put } from '@nestjs/common';
import { NamesService } from './names.service';
import { ApiBody, ApiOperation, ApiParam, ApiQuery, ApiTags } from '@nestjs/swagger';

@Controller('api/v1/names')
@ApiTags('names')
export class NamesController {

    // inyectamos un servicio
    constructor(private namesService: NamesService) {

    }

    @Post() // creamos un decorador 
    @ApiBody({
        description: 'Añadiendo un nombre',
        examples: {
            ejemplo1: {
                value: {
                    name: 'Dairan'
                }
            },
            ejemplo2: {
                value: {
                    name: 'Josue'
                }
            }
        }
    })
    @ApiOperation({
        description: 'Crea un nuevo nombre. Retorna true cuando se inserta correctamente. Retorna true si se realiza correctamente'
    })
    createName(@Body() data: {name: string}) { 
        return this.namesService.createName(data.name);
    }    

    @Get()
    @ApiQuery({
        name: 'start',
        type: 'string',
        required: false,
        description: 'Nombre por el que empieza el query.'
    })
    @ApiOperation({
        description: 'Devuelve todos los nombres.'
    })
    getNames(@Query('start') start: string) {
        return this.namesService.getNames(start);
    }

    @Put('/:name/:newName')
    @ApiParam({
        name: 'name',
        type: 'string',
        description: 'nombre original'
    })
    @ApiParam({
        name: 'newName',
        type: 'string',
        description: 'nombre nuevo'
    })
    @ApiOperation({
        description: 'Actualiza el nombre del primer parametro por el nombre del segundo.'
    })

    uptdateName(@Param('name') name: string, @Param('newName') newName: string) {
        return this.namesService.updateName(name, newName);
    }

    @Delete('clear')
    @ApiOperation({
        description: 'Elimina todos los nombres'
    })
    clearNames() {
        return this.namesService.clearNames();
    }

    @Delete('/:name')
    @ApiParam({
        name: 'name',
        type: 'string',
        description: 'nombre a eliminar'
    })
    @ApiOperation({
        description: 'Elimina el nombre pasado como parámetro. Retorna true si lo elimina.'
    })
    deleteName(@Param('name') name: string) {
        return this.namesService.deleteName(name);
    }

}
